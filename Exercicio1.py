'''
Enunciado

Antecessor e Sucessor de um número
Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.
Média de 4 notas
Escreva um programa em Python que leia quatro números e calcule a média entre esses números
'''

num1 = int(input('Digite um número: '))

print(f'O número antecessor é {num1 - 1} e o sucessor é {num1 + 1}')


# Alternativa 1
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))
numero4 = float(input('Digite o quarto número: '))
media = (numero1 + numero2 + numero3 + numero4) / 4
print(f'A média dos números {numero1, numero2, numero3, numero4} é {media:.2f}')

#Alternativa 2

# numero1 = float(input('Digite o primeiro número: '))
# numero2 = float(input('Digite o segundo número: '))
# numero3 = float(input('Digite o terceiro número: '))
# numero4 = float(input('Digite o quarto número: '))
# media = numero1 + numero2 + numero3 + numero4
# print(f'A média dos números {numero1, numero2, numero3, numero4} é {media / 4}')