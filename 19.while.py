#Incremento ou decremento de uma condição
gameName = input('Digite o nome do jogo: ')
qtqRating = 0
totalRating = 0
rating = 0
avarange = 0

while(rating != -1):
    rating = float(input('Informe a nota do jogo: '))
    if(rating != -1):
        totalRating += rating #totalRating = totalRating + rating
        qtqRating += 1 #qtdRating = qtdRating = 1
        avarange = totalRating / qtqRating
print(f'Média das avaliações do jogo {gameName} é {avarange:.2f}')