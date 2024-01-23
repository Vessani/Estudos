#Condições if e else podem ser usadas de várias maneiras geralmente são usadas como condições Se -> Se não.
name = input('Digite o nome do jogo: ')
yearLaunch = int(input('Digite o ano do jogo: '))
classification = float(input('Digite a nota de classificação do jogo: '))

if classification > 8.0 and yearLaunch > 2015:
    print(f'O jogo {name} é bom. Recomendo joga-lo')
else:
    print(f'O jogo {name} ainda não atingiu uma boa nota. Por isso não recomendo')
    