# Author:Clive Chen
# if...elif...else

age_of_boy = 56

'''
count = 0
while count < 3:
    guess_age = int(input("guess age:"))

    if guess_age == age_of_boy:
        print("yes, you got it.")
        break
    elif guess_age > age_of_boy:
        print("think smaller...")
    else:
        print("think bigger...")
    count = count +1 #count +=1
#if count == 3:  用以下判断语句更优化
else:
    print("you have tried too many times...!")
'''

'''
count = 0
for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_boy:
        print("yes, you got it.")
        break
    elif guess_age > age_of_boy:
        print("think smaller...")
    else:
        print("think bigger...")
else:
    print("you have tried too many times...!")
'''

count = 0
while count < 3:
    guess_age = int(input("guess age:"))

    if guess_age == age_of_boy:
        print("yes, you got it.")
        break
    elif guess_age > age_of_boy:
        print("think smaller...")
    else:
        print("think bigger...")
    count = count +1 #count +=1
    if count == 3:
        continue_confirm = input("do you want to keep guessing...?Y/N")
        if continue_confirm != 'n':
            count = 0
else:
    print("you have tried too many times...!")