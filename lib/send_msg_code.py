import requests
import random
import datetime
import time
import hashlib
import json




def rand_code(num=4):
    '''
    :param num:多少位的数字验证码
    :return:一个验证码字符串
    '''
    msg_code = []
    for i in range(num):
        msg_code.append(str(random.randint(0,9)))

    return "".join(msg_code)

class SendMsg(object):
    def __init__(self):
        self._appid = "xxx"
        self._appkey = "xxx"

    def send(self,phone):
        msg_code = rand_code()
        random_num= str(int(time.time()))
        strTime = str(int(time.time()))
        self._url = "https://yun.tim.qq.com/v5/tlssmssvr/sendsms?sdkappid=%s&random=%s" % (self._appid,random_num)
        strMobile = phone
        sig_str = "appkey=%s&random=%s&time=%s&mobile=%s"%(self._appkey, random_num, strTime,phone)

        sig = hashlib.sha256(sig_str.encode("utf-8")).hexdigest()
        data ={
            "params":[msg_code,"1"],
            "tpl_id":000,
            "sig":sig,
            "tel":{
                "mobile": strMobile,
                "nationcode": "86"},
            "time":strTime,
            "type":0,
            "random":random_num,
        }
        result_code = None
        try:
            r = requests.get(self._url, json=data)
            result_json = json.loads(r.text)            # result_json格式 {'result': 0, 'errmsg': 'OK', 'sid': '8:jTKb7h9xLlf7MQi8XeX20180410', 'fee': 1}
            return result_json,msg_code
        except:
            return result_code,None



if __name__  == "__main__":
    phone = "15xxxxxxxx"
    # a = SendMsg().send(phone)
    # a = json.loads(a[0])

    pass
