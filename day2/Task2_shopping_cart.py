# Author:Clive Chen

'''
1. iphone         5800
2. mac pro        12000
3. Starbuck Latte 31
4. Alex Python    81
5. Bike           800
'''

product_list = [
    ('iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Python_Book',50),
]
shopping_list = []
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        #for item in product_list:
        for index,item in enumerate(product_list):
            #print(product_list.index(item),item)
            print(index,item)
        user_choice = input("选择你需要的商品序号>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary: #买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦,还买个毛线!\033[0m" % salary)
            else:
                print("product code [%s] is not exist!" %user_choice)
        elif user_choice == 'q':
            print("--------shopping list---------")
            for p in shopping_list:
                print(p)
            print("Your crrent balance:",salary)
            exit()
        else:
            print("invalid option!")



'''
程序启动：
Your Salay:5000
>>>:1      #工资里减掉选择的物品
added [iphone] to your shopping cart

1. iphone         5800
2. mac pro        12000
3. Starbuck Latte 31
4. Alex Python    81
5. Bike           800
>>>:5   提示余额不足。。。
继续循环
q  退出
已买清单和总价
打印以下清单
have bought below:
[[iphone,5800],[coffee,31]]
your balance:399
'''