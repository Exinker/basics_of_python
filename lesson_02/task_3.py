number = int(input('Номер месяца: '))

# list variante
seasons = ['зима', 'весна', 'лето', 'осень']
season = seasons[(number % 12) // 3]

print(season)

# dict vatiante
seasons = {
    0: 'зима',
    1: 'весна',
    2: 'лето',
    3: 'осень'
}
season = seasons[(number % 12) // 3]

print(season)
