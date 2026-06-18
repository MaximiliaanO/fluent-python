import typing

class City(typing.NamedTuple):
    continent: str
    name: str
    country: str

cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'Sao Paulo', 'BR'),
]

def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City('Asia'): # Matches a City instance where the first attribute value equals 'Asia' regardless of the other attributes.
                results.append(city)

    return results

x = match_asian_cities()
print(x)

def match_asian_countries_pos():
    results = []
    for city in cities:
        match city:
            case City('Asia', _, country):
                results.append(country)

    return results

y = match_asian_countries_pos()
print(y)
