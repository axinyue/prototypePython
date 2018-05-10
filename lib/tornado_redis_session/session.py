# coding:utf-8
import random
import datetime
from hashlib import sha1

import redis
from tornado.web import RequestHandler

class Expires(object):

    def cookie_expires(self,expires_days=None,expires=None):
        times_seconds = datetime.datetime.now()
        if (expires_days is None) and (expires is None):
            times_seconds = times_seconds+datetime.timedelta(seconds=1800)
        if expires_days is None:expires_days = 0

        times_seconds = times_seconds+datetime.timedelta(days=expires_days)
        if expires:
            times_seconds= times_seconds+datetime.timedelta(seconds=expires)

        return times_seconds

    def session_expires(self,expires_days=None,expires=None):
        times_seconds = 0
        if expires_days:
            times_seconds += 86400*expires_days
        if expires:
            times_seconds += expires
        return times_seconds

_expire = Expires()

class SessionManager(object):
    def __init__(self, redis):
        self.redis = redis

    def set_session(self, sessionid, identifier, ctx, expires=None):
        self.redis.hset("session:%s" % sessionid, identifier, ctx)
        if expires:
            self.redis.expire("session:%s" % sessionid, int(expires))

    def get_session(self, sessionid, identifier):
        ctx = self.redis.hget("session:%s" % sessionid, identifier)
        return ctx

    def clear(self, sessionid, identifier):
        self.redis.hdel("session:%s" % sessionid, identifier)

    def clear_all(self, sessionid):
        self.redis.delete("session:%s" % sessionid)


class RedisSessionHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        super(RedisSessionHandler, self).__init__(*args, **kwargs)
        _redis = redis.Redis(**self.settings['redis'])
        self.__session_manager = SessionManager(_redis)

    def get_sessionid(self):
        return self.get_cookie('sessionid')

    def __gen_sessionid(self):
        salt = "-".join((
            str(datetime.datetime.now()),
            str(random.random()),
            self.request.remote_ip,
            self.settings.get("cookie_secret")
        ))
        sessionid = sha1(salt.encode("utf-8")).hexdigest()
        sessionid = "%s" % sessionid
        return sessionid

    def get_session(self, key):
        sessionid = self.get_sessionid()

        if sessionid:
            kv = self.__session_manager.get_session(sessionid, key)
            return kv

    def set_session(self, key, value,session_expires=None,cookie_expires=None,cookie_expires_day=None,session_expires_days=None):
        cookie_expires = _expire.cookie_expires(expires_days=cookie_expires_day,expires=cookie_expires)
        session_expires = _expire.session_expires(expires_days=session_expires_days,expires=session_expires)
        #self.clear_all_session()
        sessionid = self.get_sessionid()
        if not sessionid:sessionid = self.__gen_sessionid()      # 更改 每次设置都生成一个新的id
        self.set_cookie('sessionid', sessionid,expires=cookie_expires)
        return self.__session_manager.set_session(sessionid, key, value,expires=session_expires)

    def clear_session(self, key):
        sessionid = self.get_sessionid()
        return self.__session_manager.clear(sessionid, key)

    def clear_all_session(self):

        sessionid = self.get_sessionid()
        return self.__session_manager.clear_all(sessionid)
