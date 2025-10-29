num = 4
print(num)
num = 7
print(num)

# Rules: 
# 1. variable name can't be start from number, special charater can be used in start or anywhere (letter and underscore _ valid start)

user_name = "Arun"  # snake case writing
userName = "Arun"  # camle case writing

# concatination of string 

name =  "arun" + "kumar"

print(name) # valid

#print(name + 3) # error

print(name + "3") # valid

# User Inpur function 
# only string can be taken as a input

num1 = int(input("Please enter first number: " ))
num2 = int(input("Please enter second number: " ))
sum = num1 + num2

print("the addition is " + str(sum))

name , age = "arun" , 30

print("my names is " + name + " and my age is " + str(age) )

a=b=c=4

print(a+b+c)

name , age = input("Please enter your namee and age: ").split()
name , age = input("Please enter your namee and age: ").split(":")

print(name)
print(age)
