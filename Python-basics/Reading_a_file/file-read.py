f = open('file.txt', 'r')
print(f.name)
f.close()

with open('file.txt', 'r') as file:
    pass
print(file.closed)
print(file.read())