# Let’s make your “Hello World + system info” Python script step-by-step.
import os
import platform
import datetime
print('hello world')

print('\nThe system parameters are : ')
print("-" * 30)

print(f'The opearting system and release version is : {platform.system()} {platform.release()} {platform.version()}' )
print('The ')
print(f"The release version of os is : {platform.release()} " )
print(f"The cpu count: {os.cpu_count()}")
print(f"The curent time : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")