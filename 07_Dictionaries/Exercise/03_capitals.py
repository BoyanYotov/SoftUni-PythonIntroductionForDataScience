countries = list(input().split(', '))
capitals = list(input().split(', '))

result = dict(zip(countries, capitals))

for k, v in result.items():
    print(f'{k} -> {v}')
