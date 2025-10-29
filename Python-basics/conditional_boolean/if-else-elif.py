if True:
     print("abnhd")

user = 'arun'
logged_in = False

if user == 'arun' and logged_in:
    print("Arun is looged in")
else:
    print("Please log in",user)

user = 'arun'
logged_in = True

if user == 'arun' and logged_in:
    print(f"{user} is looged in")
else:
    print("Please log in",user)

a = [1, 2, 3]
b = [1, 2, 3]

if a == b:
    print('Ture')

print(a is b)  
print(id(a))
print(id(b))

a = [1, 2, 3]
b = a

print(a is b)  
print(id(a))
print(id(b))

a = [1, 2, 3]
b = a

print(a == b)  
print(id(a))
print(id(b))


# $ python if-else-elif.py 
# abnhd
# Please log in arun
# arun is looged in
# Ture
# False
# 2410956939712
# 2410957089344
# True
# 2410959554944
# 2410959554944
# True
# 2410957089344
# 2410957089344