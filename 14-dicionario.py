#Dicionário são usados para armazenar valores em chaves, eles são ordenados e mutavel, não poder ser repitidos
gameFifa = {
    'name': 'Fifa 23',
    'yearLauch': 2023,
    'gamePrice': 90.50,
    'classification': 8.5,
    'genre': ['Esporte', 'Familia']
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

#Recuperar um elemento do dicionário

print(gameFifa['genre'])
print(gameFifa.get('classification'))

#Busca apenas as chaves do dicionário

print(gameFifa.keys())

#Busca apenas os valores do dicionário

print(gameFifa.values())

#Busca apenas os itens do dicionário com chave e valor

print(gameFifa.items())


#Adicionar itens ao dicionário

gameFifa['Players'] = 2
print(gameFifa)

#Atualizar itens no dicionário
gameFifa.update({'Players' : 1})
print(gameFifa)

#Remover um item do dicionário

gameFifa.pop('Players')
print(gameFifa)