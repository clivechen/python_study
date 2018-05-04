# Author:Clive Chen
# 调库/getpass/if...else
import getpass  #调入库

#username = input("username:")
#password = input("password:")
#print (username,password)

_username = "clive"
_password = "abc123"
username = input("username:")
password = getpass.getpass("password:")   #输入时不显示明文密码
print (username,password)

if _username == username and _password == password:
    print("Welcome user {name} login ..." .format(name=username))
else:
    print("Invalid username or password!")