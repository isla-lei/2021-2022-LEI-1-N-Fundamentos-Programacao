"""Lista 07-Ciclos - Exercicio 4.

Escreva um programa que leia uma sequência de números inteiros terminada em zero e calcule: 
-máximo, 
-mínimo, 
-a soma dos números introduzidos, 
-total dos números pares e ímpares introduzidos
"""

numero = -1
contador = 0
soma = 0
max = min = 0;
conta_pares = conta_impares = 0

while numero != 0:
    numero = int(input(str(contador+1) + "º número: "))

    # verficar se numero diferente de zero
    if numero != 0:   
        # max e min     
        # o 1º numero é max e min 
        if contador == 0:
            max = numero
            min = numero
        
        if numero > max:
            max = numero
        if numero < min:
            min = numero

        # par e impar
        if numero % 2 == 0:
            conta_pares += 1 # conta_pares = conta_pares + 1
        else:
            conta_impares += 1 # conta_impares = conta_impares + 1
            
        soma = soma + numero
        contador = contador + 1

print()
print("   E S T A T I S T I C A S ")
print("==============================")

print("Quantidade de números..:", contador)
print("Soma...................:", soma)
print("Média..................:", "{:.2f}".format(soma / contador) )
print("Máximo.................:", max)
print("Minimo.................:", min)
print("Quantidade de pares....:", conta_pares)
print("Quantidade de impares..:", conta_impares)
