gameName = 'Fifa 23'
gameDescription = '''
Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports, que possibilita jogar online ou localmente
'''

print(gameName.upper()) #Retorna a string em maiusculo
print(gameName.lower()) #Retorna a string em minusculo
print(gameName.capitalize()) #Retorna a primeira letra em maiusculo
print(gameName.title()) #Retorna a primeira letra em maiusculo
print(gameName.center(10, '-')) #Retorna a string centralizada com preenchimento de caracter
print(gameName.find('a')) #Retorna a posição onde foi encontrado o caracter
print(gameDescription.count('f')) #Retorna uma contagem de um caracter
print(gameDescription.count('a')) #Retorna uma contagem de um caracter
print(gameName.replace('Fifa', 'Pes')) #Altera um elemento por outro
print(gameName.split(',')) #Quebra a string em partes menores neste caso utilizando ','