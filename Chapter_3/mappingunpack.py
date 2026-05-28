def dump(**kwargs):
    return kwargs

x = dump(**{'x':1}, y=2, **{'z':3, 'f':4})
print(x)

a = {'a':2, 'b':3, 'C':4}

y = dump(**a)
print(y)

