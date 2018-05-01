# Author:Clive Chen
import getpass

#usename = input("username:")
#password = input("password:")
#print (usename,password)

usename = input("username:")
password = getpass.getpass("password:")   #输入时不显示明文密码
print (usename,password)