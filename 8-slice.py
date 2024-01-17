#Gerando uma substring em uma string. Em python fazemos isso usando o método slice
gameName = 'Fifa 23'
gameDescription = '''
Fifa 23 é um jogo de futebol desenvolvido pela EA Sports
e que possibilita jogar online ou localmente
'''
#Slice [Inicio : Fim] - O indice inicia em 0 e finaliza em -1   

#Busque toda uma string a partir da primeira posição

print(gameName[0:])

#Busque uma string até a ultima posição

print(gameName[:7])

# Busque da terceira até a ultima posição
print(gameName[2:])

#Incrementando. Por padrão ele é 1.

#Busque toda uma string de 2 em 2 caracteres
print(gameName[::2])

#Busque toda uma estring nos indices impares
print(gameName[1::2])

#Inverter uma string de trás para frente

print(gameName[:: -1])