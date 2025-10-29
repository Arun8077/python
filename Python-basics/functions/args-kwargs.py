# def student(*args, **kwargs):
#     print(args)
#     print(kwargs)
# student('Math', 'physics' , name='arun', age='30')

# $ python args-kwargs.py   ---> 
# ('Math', 'physics')             -----> A tuple o/p
# {'name': 'arun', 'age': '30'}   -----> A dict o/p

# def student(*args, **kwargs):
#     print(args)
#     print(kwargs)

# cources = ['Math', 'physics']
# info = {'name': 'arun', 'age': '30'}

# student(cources, info)

# $ python args-kwargs.py 
# (['Math', 'physics'], {'name': 'arun', 'age': '30'})
# {}

def student(*args, **kwargs):   ## for accepting the arbitary Input
    print(args)
    print(kwargs)

cources = ['Math', 'physics']
info = {'name': 'arun', 'age': '30'}

student(*cources, **info)  ## For unpacking the values.

# akssh@Arun_PC MINGW64 /e/git-3273/repositories/python/Python-basics/functions (branch1)
# $ python args-kwargs.py 
# ('Math', 'physics')
# {'name': 'arun', 'age': '30'}
