name_city = input('\nType a name of a city: ')

starts_with_santo = name_city.split()[0].lower() == 'santo'

if starts_with_santo:
    print("The city name starts with SANTO")
else: 
    print("City name does not start with SANTO")