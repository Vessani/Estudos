'''
Cálculo da Distância

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas.
'''

distancia = float(input('Qual a distancia você irá percorrer? '))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.35
    
print(f'A distancia da viagem é de {distancia} KM o valor da viagem será R$ {passagem:.2f}')



'''
Aumento salário funcionário

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.
'''

salario = float(input('Informe o valor do seu salário: '))

if salario <= 1250:
    aumento = salario * 0.15    
else:
    aumento = salario * 0.10
    
print(f'O seu salário é de {salario} e o seu aumento é de {aumento}')