from tornado.web import RequestHandler


import redis
from setting import REDIS_CONFIG


class MyRedis(RequestHandler):
    def __init__(self,*args,**kwargs):
        super(MyRedis, self).__init__(*args, **kwargs)
        self._redis = redis.Redis(**self.settings['redis'])

    def set_redis(self,rediskey, identifier, ctx, expires=None):
        self._redis.hset(rediskey,identifier, ctx)
        if expires:
            self._redis.expire(rediskey,int(expires))

    def get_redis(self,rediskey,identifier):
        ctx = self._redis.hget(rediskey, identifier)
        return ctx


class OperRedis():
    def __init__(self):
        self._redis = redis.Redis(**REDIS_CONFIG)

    def set_redis(self,rediskey, identifier, ctx, expires=None):
        self._redis.hset(rediskey,identifier, ctx)
        if expires:
            self._redis.expire(rediskey,int(expires))

    def get_redis(self,rediskey,identifier):
        ctx = self._redis.hget(rediskey, identifier)
        return ctx
