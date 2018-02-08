import hmac
message = b'Hello,World'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())                                                                                        # 9526c82a8036af370b95f5c3238e58f1


import hashlib
md5 = hashlib.md5()                                                                                     # MD5
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())                                                                                  # d26a53750bc40b38b65a520292f69306
print(len("d26a53750bc40b38b65a520292f69306"))                     # 32

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))                            # 如果很长则可以分多次来update
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())                                                                                  # d26a53750bc40b38b65a520292f69306
print(len("d26a53750bc40b38b65a520292f69306"))                      # 32

sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())                                                                                 # b752d34ce353e2916e943dc92501021c8f6bca8c
print(len("b752d34ce353e2916e943dc92501021c8f6bca8c"))      # 40

sha256 = hashlib.sha256()
sha256.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha256.hexdigest())                                                                            # 4ea74ff8a47fc7553d4c6eafca460cb99fbd80694ba907217b87c9d4e47cb2f7
print(len("4ea74ff8a47fc7553d4c6eafca460cb99fbd80694ba907217b87c9d4e47cb2f7")) # 64

db = {                                                                                                              # 模仿安全登录
    'michael': 'e10adc3949ba59abbe56e057f20f883e',      #123456
    'bob': '878ef96e86145580c38c87f0410ad153',              #abc999
    'alice': '99b1c2188db85afee403b1536010c2c9'             #alice2008
}

def calc_md5(psw):
    md5 = hashlib.md5()
    md5.update(psw.encode('utf-8'))
    return md5.hexdigest()

def login(user,psw):
    psw = calc_md5(psw)
    user_collection = db.keys()
    if user in user_collection :
        if db[user] == psw:
            print('Login success')
        else:
            print('Password error')
    else:
        print("User doesn't exits")

login('bob','abc999')


c = {}

def calc_md5_sault(user,psw):
    return calc_md5(psw+user+"python")

def register(user,psw):
    c[user] = calc_md5_sault(user,psw)

def login2(user,psw):
    psw = calc_md5_sault(user,psw)
    user_collection = c.keys()
    if user in user_collection :
        if c[user] == psw:
            print('Login success')
        else:
            print('Password error')
    else:
        print("User doesn't exits")

register("Mike","12345")
register("Jack","12345")
print(c)

login2("Mike","12345")