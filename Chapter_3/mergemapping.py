print("""
d1 = {'a':1, 'b':3}
d2 = {'a':2, 'b':5, 'c': 6}
""")

d1 = {'a':1, 'b':3}
d2 = {'a':2, 'b':5, 'c': 6}
x = d1 | d2
d1 |= d2


print(f'This is d1 | d2 stored in variable x: {x}')

print(f'This is d1 |= d2 printing d1: {d1}')
print(f'This is d1 |= d2 printing d2: {d2}, d2 is unchanged')