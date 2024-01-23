#Condições elif 

num1 = float(input('Informe o valor: \n'))
num2 = float(input('Informe outro valor: \n'))

operation = input('Digite a operação que deseja realizar: ( + - * / ) \n')

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else: 
    print('Operação invalida')
    result = 0
    
print(f'O resultado é: {result:.2f}')


