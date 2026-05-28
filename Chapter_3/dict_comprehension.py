DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

country_dail ={country:code for code, country in DIAL_CODES}
print(country_dail + "\n")

print(sorted(country_dail.items()))

country_sorted = {code: country.upper()
                  for country, code in sorted(country_dail.items())
                  if code < 70}

print(country_sorted)