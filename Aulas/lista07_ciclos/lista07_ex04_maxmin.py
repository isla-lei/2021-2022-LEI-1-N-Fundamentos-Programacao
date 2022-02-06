"""Lista 07-Ciclos - Exercico 4.

Escreva um programa que leia uma sequência de números inteiros
terminada em zero e calcule:
 máximo,
 mínimo,
 a soma dos números introduzidos,
 total dos números pares e ímpares introduzidos
"""

"""
numero = int(input("Numero Incial: "))
while numero != 0:
    numero = int(input("Numero loop: "))
"""

"""
numero = 1 # para ser diferente de 0, obriga a entrada no while
while numero != 0:
    numero = int(input("Numero loop: "))
"""

"""
while True:
    numero = int(input("Numero loop: "))
    if numero == 0:
        break;
"""

""""
    SOLUÇÃ0 COM O while True 
"""
soma = quant_pares = quant_impares = 0
#ou
#soma = 0
#quant_pares = 0
#quant_impares = 0

max = 0
min = 0
contador = 0

while True:

    numero = int(input(str(contador+1) + "º Numero (0 p/ terminar): "))
    if numero == 0:
       break; # Aborta loop while e salta para #1

    # caso numero não seja 0 (zero)
    soma = soma + numero

    # verificar se numero é par
    if numero % 2 == 0:
        quant_pares = quant_pares + 1
    else:
        quant_impares = quant_impares + 1

    # Max e Min
    # considerar o 1º numero como max e min
    if contador == 0:
        max = numero
        min = numero

    if numero > max:
        max = numero

    if numero < min:
        min = numero

    contador = contador + 1
    # FIM do ciclo while

#1
print()
print("====ESTATISTICAS====")
print("Quantidade..........:  " + str(contador))
print("Soma................: ", soma)
print("Quantidade Pares....: ", quant_pares)
print("Quantidade Impares..: ", quant_impares)
print("Máximo..............: ", max)
print("Minimo..............: ", min)
