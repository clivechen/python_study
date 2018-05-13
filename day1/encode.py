# Author:Clive Chen

'''
>>> '€20'.encode('utf-8')
b'\xe2\x82\xac20'

>>> b'\xe2\x82\xac20'.decode('utf-8')
'€20'
'''

msg = "我爱你中国！"
print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))