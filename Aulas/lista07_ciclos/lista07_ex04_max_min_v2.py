"""Lista 07 Ex04 - MaxMin

Escreva um programa que leia uma sequência de números inteiros 
terminada em zero e calcule:
- máximo,
- mínimo,
- a soma dos números introduzidos,
- total dos números pares e ímpares introduzidos

"""


soma = 0
contador = 0
max = 0
min = 0
total_pares = 0
total_impares = 0

while True:# cria um loop infinito, temos que definir criterio de termino
    numero = int(input(str(contador+1) + "º Numero: "))

    # definir criterio de termino
    if numero == 0:
        break # termina o ciclo

    soma = soma + numero

    #max e min
    if numero > max or max == 0:
        max = numero
    if numero < min or min == 0:
        min = numero

    # par / impar
    if numero % 2 == 0:
        total_pares = total_pares + 1
    else:
        total_impares = total_impares + 1

    contador = contador + 1 # contador +=1
    # fim ciclo while

print()
print("E S T A T I S T I C A S")
print("=======================")
print(f"Quantidade.....: {contador}")
print(f"A soma é.......: {soma}")
print(f"Maximo.........: {max}")
print(f"Minimo.........: {min}")
print(f"Total pares....: {total_pares}")
print(f"Total impares..: {total_impares}")