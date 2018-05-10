import requests
import random

userId="xiaohuan2"
key ="54e4bd2d89c5cc79e3a9"

def rand_code(num=4):
    '''
    :param num:多少位的数字验证码
    :return:一个验证码字符串
    '''
    msg_code = []
    for i in range(num):
        msg_code.append(str(random.randint(0,9)))

    return "".join(msg_code)

def send_msg_code(phone,msg="验证码"):
    url = "http://utf8.api.smschinese.cn/"
    data ={
        "Action":"UP",
        "Uid":userId,
        "Key":key,
        "smsMob":phone,
        "smsText": "%s:%s"%(msg,rand_code())
    }
    return requests.get(url,data=data)

if __name__  == "__main__":
    pass
