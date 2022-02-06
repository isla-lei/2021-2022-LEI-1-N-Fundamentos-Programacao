
print (' \n Este programa vai calcular o seu peso ideal \n')
altura = float(input('Insira a sua altura: \n'))
Sexo = input('Insira o seu sexo M ou F: \n')

if (Sexo == 'M' or Sexo == 'm'):
    pesoideal = (72.7 * altura) - 58 
    print (f'Peso ideal para uma homem é {pesoideal:.2f}')

elif (Sexo == 'F' or Sexo == 'f'):
    pesoideal=(62.1 * altura) - 44.7
    print (f'Peso ideal para uma mulher é {pesoideal:.2f}')
else:    
    print('Genero invalido')