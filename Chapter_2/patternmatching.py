metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.61889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9} | {"coordinates"}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat,lon) as coord] if lon <=0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f} | {coord}')

# In general, a sequence pattern matches the subject if:
# 1. The subject is a sequence and;
# 2. The subject and the pattern have the same number of items and;
# 3. Each corresponding item matches, including nested items.
# The pattern [name, _, _, (lat,lon)] matches a sequence with four items, and the last item must be a two-item sequence.
# It doesn't matter if a sequence pattern is a () or a [] because in a sequence pattern they mean the same thing.



if __name__ == '__main__':
    main()