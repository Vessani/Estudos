# Similar a lista porém com algumas limitações, diferente da lista está usa () em vez de []. Não conseguimos adicionar, remover, ordenar itens numa tupla

gamesTuple = ('Fifa 23', 'GTA V', 'Red Dead 2', 'Stars Wars', 'Call of Duty')
print(type(gamesTuple))

#Buscar os dois primeiros itens 

print(gamesTuple[:2])

#Buscar o último item da lista

print(gamesTuple[-1])

#Buscar até determinado item

print(gamesTuple[1:4])

#Buscar de uma posição em diante

print(gamesTuple[2:])

#Recuperar um item da tupla pelo indice

print(gamesTuple.index('Stars Wars'))