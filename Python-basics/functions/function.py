# ## some instruction togather to perform some action

# def hello_fn():
#     pass

# print(hello_fn)  ## No valid output

# print(hello_fn())
# hello_fn()

# def hello_fn():
#     print('Hello from function!')

# hello_fn()

def hello_fn():
    return 'Hi'

hello_fn()

# In Python, a return sends a value back to where the function was called.
# It does not automatically print anything to the screen.

# Since you didn’t store or print the returned value, Python just returns 'Hi' silently and moves on.

# That’s why you see no output.



# def hello_fn(arg1, arg2='default_value'):
#     return 'Hi ' '{} {}'.format(arg1,  arg2)

# print(hello_fn('Akash', 'bhai'))


def hello_fn(arg1, arg2='default_value'):
    return 'Hi ' '{} {}'.format(arg1,  arg2)

print(hello_fn('Akash', arg2='bhai'))

