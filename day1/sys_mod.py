# Author:Clive Chen

import os
#cmd_res = os.system("dir")  #执行命令，不保存结果
cmd_res = os.popen("dir").read()   #read从内存空间读取数据
print("--->",cmd_res)
os.mkdir("dir_new")