import hashlib


def fun(str_a):
    m = hashlib.md5()
    m.update(str_a.encode("utf-8"))
    psw = str(m.hexdigest())
    return psw

a = fun("asdf")
print(a)
b = fun(a)
print(b)
print(36**8)
print(len("5259ee4a034fdeddd1b65be92debe731"))