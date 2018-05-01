# Author:Clive Chen
#if...elif...else

age_of_boy = 56

guess_age = int(input("guess age:"))

if guess_age == age_of_boy:
    print("yes, you got it.")
elif guess_age > age_of_boy:
    print("think smaller...")
else:
    print("think bigger...")
