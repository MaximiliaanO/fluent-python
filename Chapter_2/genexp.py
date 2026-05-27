import array

symbols = '$¢£¥€¤'
x = tuple((ord(symbol) for symbol in symbols))
print(x)

y = array.array('I', (ord(symbol) for symbol in symbols))
print(y)

colors = ['black', 'white',]
sizes = ['S', 'M', 'L',]

for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)