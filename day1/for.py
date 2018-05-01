# Author:Clive Chen
'''
for i in range(0,10,2): #最三个为步进
    print("loop",i)
'''

'''
for i in range(0,10):
    if i < 5:
        print("loop",i)
    else:
        continue    #跳出本次循环，break跳出整个循环
    print("hehe...")
 '''
'''
for i in range(10):
    if i < 5:
        print("loop",i)
    else:
        continue
    print("hehe...")
'''

for i in range(10):
    print("-----------------",i)
    for j in range(10):
        print(j)
        if j > 5:
            break
