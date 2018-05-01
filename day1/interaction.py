# Author:Clive Chen

name = input("Name:")
#raw_input 2.x input 3.x
#input 2.x 查找变量非输入
age = int(input("Age:")) #integer
#print (type(age)) #打印变量类型
job = input("Job:")
salary = int(input("Salary:"))

#info = '''
#--------------info of '''+ name +''' -------------
#Name:'''+ name +'''
#Age:'''+ age +'''
#Job:'''+ job +'''
#Salary:'''+ salary +
#'''
#print (info)

info = '''
--------------info of %s -------------
Name:%s
Age:%d
Job:%s
Salary:%d
'''%(name,name,age,job,salary)

print (info)

#格式化输出

info2 = '''
--------------info2 of {_name} -------------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)
print (info2)

info3 = '''
--------------info3 of {0} -------------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)
print (info3)