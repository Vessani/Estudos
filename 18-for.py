gameList = ['Fifa', 'God of War', 'Call of Duty', 'Hogwarts Legacy']
#Iterando valores de uma lista
for game in gameList:
    print(game)
    
#Quando a condição for atendida, o loop sera encerrado

for game in gameList:
    if game == 'Call of Duty':
        break
    print(game)

#Quando a condição for atendida, o loop irá para a proxima iteração

for game in gameList:
    if game == 'God of War':
        continue
    print(game)
    
#Avaliação do jogo
gameName = input('Digite o nome do jogo: ')
gameRating = int(input('Digite quantas notas você deseja fazer no jogo: '))

sum = 0 #Incrementa o valor das notas
for i in range(gameRating):
    note = float(input('Digite a nota do jogo: '))
    sum += note # sum = sum + note
print(f'Média de avaliação de jogo {gameName} é {sum/gameRating:.2f}')
    
