'''
Exercicio 2:

Substituindo caracter repitido:

Escreva um progama em python para obter uma string de uma determinada string em que todas as ocorrencias de seu primeiro caracter foram alterados para $, exceto o primeiro caracter
Ex: fifa 23 -> fi$a 23

Troca de caracter

Escreva um programa em python para obter uma unica string de duas strings fornecidas sepadaras por um espaço e troque os dois primeiros caracteres de cada string.
Ex: abc xyz -> xyc abz


'''
# Parte1
name = input('Digite o nome do jogo: ')
#Transforma o primeiro caracter em minuscula
char = name[0].lower()
#Altera um caracter no elemento name.
new_name = name.replace(char, '$')
#Concatena os elementos
new_name = char + new_name [1:]
print(new_name)

#Parte2
st1 = 'agc' #pxc
st2 = 'pxs' #ags


new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print(new_st1)
print(new_st2)