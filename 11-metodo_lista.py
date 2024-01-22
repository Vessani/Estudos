# Tipo de dados em lista

gameList = ['Residente Evil 4', 'Star Wars', 'Call of Duty 3', 'Battlefield 2042', 'Hogwarts Legacy', 'Fortinite']

#Tamanho da lista
print(len(gameList))

#Recuperar um item da lista pelo indice

print(gameList.index('Hogwarts Legacy'))

#Adicionar um item ao final da lista
gameList.append('GTA 5')
print(gameList)

#Ordenar lista
gameList.sort()
print(gameList)

#Copiar itens de uma lista para outra e remover um item da lista
gameReset = gameList.copy()
gameReset.remove('Hogwarts Legacy')
print(gameReset)
