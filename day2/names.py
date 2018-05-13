# Author:Clive Chen
import copy
#names = "Zhangyang Guyun Xiangpeng Xuliangchen"
names = ["Zhangyang","Chenronghua","Guyun","Xiangpeng",["alex","jack"],"Xuliangchen"]
#names2 = [1,2,3,4]
#names.append("Leihaidong")  #追加
#names.insert(2,"Chenronghua")  #插入
#names.insert(3,"Xinzhiyu")  #一次只能插入一条"
#names[4] = "Xiedi" #替换
#names.remove("Chenronghua") #删除1
#del names[2] #删除2
#names.pop(3) #删除3

#print(names)
#print(names.index("Xiedi")) #查找位置
#print(names[names.index("Xiedi")]) #查找位置并打印（是否多此一举？）
#print(names.count("Chenronghua")) #统计次数
#names.clear() #清空
#names.reverse() #反转
#names.sort() #排序
#names.extend(names2) #扩展

#names2 = names.copy() #复制 浅copy只拷贝第一层（子列表只是一个内存指针非实际数据）
names2 = copy.copy(names) #复制 浅copy只拷贝第一层（子列表只是一个内存指针非实际数据）
print(names)
print(names2)
names[1] = "陈荣华"
names[4][0] = "ALEX"
print(names)
print(names2)
names2 = copy.deepcopy(names) #复制 深copy重新开辟独立内存空间
print(names2)
print(names[0:-1:2])
print(names[::2])
print(names[:])
for i in names:
    print(i)

#print(names[0],names[2])
#print(names[1:2])
#print(names[1:3]) #切片--顾头不顾尾
#print(names[-1]) #最后一个值
#print(names[-3:-1]) #倒数第二第三个值
#print(names[-2:]) #最后两个值
#print(names[:3]) #前三个值