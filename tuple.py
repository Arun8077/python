cources = ('history', 'math', 'eng', 'hindi')
cources_2 = ('cs', 'it')
# cources_2[0] = 'cs' ## TypeError: 'tuple' object does not support item assignment */
# print(cources)
# print(cources_2) 
# sorted_cource = sorted(cources)
# print(type(cources))

# for item in cources:
#     print(item)

# print(sorted_cource)
# cources_format = '{}, {} electronics'.format(cources, cources_2)
cources_format_2 = '{}, {}'.format(', '.join(cources), ', '.join(cources_2))
# print(cources_format)
# print(cources_format_2)
# print(', '.join(cources))
# print('{}, {}'.format(', '.join(cources), ', '.join(cources_2)))
print(cources_format_2)
#print(cources_format_2.split(', '))
print(''.join(cources_format_2.split(', ')))
print(' '.join(cources_format_2.split(', ')))

# 🧩 1️⃣ split() — Removes the delimiter
# 🧩 2️⃣ join() — Adds the delimiter