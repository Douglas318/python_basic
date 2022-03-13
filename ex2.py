num1 = int(input('informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
soma = num1 + num2
multi = num1 * num2 
div = num1 / num2
div_int = num1 // num2
expo = num1 ** num2 

print('A soma de {} com {} é {}'.format(num1,num2, soma))
print('A multiplicação é {}',format(multi))
print('A divisão é {}'.format(div))
print('A divisão inteira é {:.3f}'.format(div_int))
print('A exponenciação  é {}'.format(expo))
