import my_module

cources = ['math', 'science', 'english', 'hindi']

index = my_module.find_index(cources, 'hindi')
print(index)

# $ python imp_module.py 
# imported this module
# 3

# import my_module as mn

# cources = ['math', 'science', 'english', 'hindi']

# index = mn.find_index(cources, 'hindi')
# print(index)

# from my_module import find_index
# cources = ['math', 'science', 'english', 'hindi']

# index = find_index(cources, 'hindi')
# print(index)

# akssh@Arun_PC MINGW64 /e/git-3273/repositories/python/Python-basics/module-import (branch1)
# $ python imp_module.py 
# imported this module
# 3


# from my_module import find_index, test
# cources = ['math', 'science', 'english', 'hindi']

# index = find_index(cources, 'hindi')
# print(index)
# print(test)

# akssh@Arun_PC MINGW64 /e/git-3273/repositories/python/Python-basics/module-import (branch1)
# $ python imp_module.py 
# imported this module
# 3
# test string


# from my_module import *
# import sys
# print(sys.path)

# $ python imp_module.py 
# imported this module
# 3
# test string
# ['E:\\git-3273\\repositories\\python\\Python-basics\\module-import', 'C:\\Users\\akssh\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 'C:\\Users\\akssh\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 'C:\\Users\\akssh\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'C:\\Users\\akssh\\AppData\\Local\\Programs\\Python\\Python313', 'C:\\Users\\akssh\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']

# import random
# cources = ['math', 'science', 'english', 'hindi']
# print(random.choice(cources))

# import math
# radss = math.radians(90)
# print(radss)

# print(math.degrees(radss))
# print(math.sin(90.0))

# # $ python imp_module.py 
# # 1.5707963267948966
# # 90.0
# # 0.8939966636005579

# import datetime
# import calendar

# today = datetime.date.today()
# print(today)
# print(calendar.isleap(2000))
# print(calendar.isleap(2001))

# # $ python imp_module.py 
# # 1.5707963267948966
# # 90.0
# # 0.8939966636005579
# # 2025-10-29
# # True
# # False

import os
print(os.getcwd())

print(os.__file__)

# $ python imp_module.py 
# E:\git-3273\repositories\python\Python-basics\module-import
# C:\Users\akssh\AppData\Local\Programs\Python\Python313\Lib\os.py

# import antigravity