import requests
from requests.cookies import merge_cookies
import json
import time

class Cookie(object):
    def __init__(self,cookie):
        self.cookie = cookie        # cookie jar 对象
        # print("%s"%str([x for x in cookie.iteritems()]))

    def look_cookie(self):
        return "%s"%str([x for x in self.cookie.iteritems()])

    def cookies_keys(self,cookie):  # 获取cookiejar 的所有键
        return [x for x in cookie.keys()]

    def check(self,cookie):     # 根据一个cookiejar 更新cookie
        pass

    def update(self,cookie):
        self.cookie = merge_cookies(self.cookie,cookie)

    def getCookieJar(self):
        return self.cookie



if __name__ =="__main__":
    pass