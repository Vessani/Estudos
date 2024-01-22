# Utiliza as {} para definição. Não recupera valor atraves de slice(fatiamento). Não pode repetir o mesmo item da lista

gameSet = {'Fifa 23', 'Call of Duty', 'Stars Wars', 'Hogwarts Legacy', 'Fortinite'}

print(gameSet)

#Buscar o tamanho do set
print(len(gameSet))


#True e 1 são consideramos o mesmo valor
exempleSet = {'Fifa 23', True, 1, 90.50}
print(exempleSet)

#Adicionar item de outro set
gameSet.update(exempleSet)
print(gameSet)

#Remover um item

gameSet.remove(True)
gameSet.remove(90.50)

print(gameSet)