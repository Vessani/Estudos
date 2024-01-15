#Input lê dados em um programa. Importante input retorna texto como uma string
'''
Jogoteca
'''
name = input('Digite o nome do jogo:\n') #Lê a informação que o usuario ira passar. \n quebra de linha
yearLauch = int(input('Digite o ano do jogo:\n')) # int antes do input informa que ele ira ler um número inteiro
gamePrice = float(input('Digite o preço do jogo: \n')) # float indica que irá ler um número flutuante
planIncluded = input('Incluido no plano \n') 
#Imprime a mensagem na tela
print(name)
print(yearLauch)
print(gamePrice)
print(planIncluded)