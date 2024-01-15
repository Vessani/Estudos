#Input lê dados em um programa. Importante input retorna texto como uma string
'''
Jogoteca
'''
name = input('Digite o nome do jogo:\n') #Lê a informação que o usuario ira passar. \n quebra de linha
yearLauch = int(input('Digite o ano do jogo:\n')) # int antes do input informa que ele ira ler um número inteiro
gamePrice = float(input('Digite o preço do jogo: \n')) # float indica que irá ler um número flutuante
planIncluded = input('Incluido no plano \n') 
#Imprime a mensagem na tela concatenando texto com variavél

#Alternativa 1:

# print('###DADOS DO JOGO###')
# print('===============')
# print('Nome do jogo: ', name)
# print('Ano do jogo: ', yearLauch)
# print('Valor do jogo: ', gamePrice)
# print('Está incluso no plano?: ', planIncluded)

#Alternativa 2:

# print('Nome do jogo: ', name, '\nAno de lançamento: ', yearLauch, '\nValor do jogo: ', gamePrice, '\nEstá incluso no plano? ', planIncluded)

#Alternativa 3:

print(f'Nome do jogo: {name} \nAno de lançamento: {yearLauch} \nValor do jogo: {gamePrice} \nEstá incluso no plano? {planIncluded}')
#Forma mais atual de se utilizar o 'F' é uma forma de formatação para informar a variavél precisa usar as {}.