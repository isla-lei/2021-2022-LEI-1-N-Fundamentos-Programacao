"""Lista 07-Ciclos - Exercico 1.

Faça um programa que calcule a média de N números introduzidos
pelo utilizador.
O valor para N é pedido ao utilizador.
"""

n = int(input("Quantidade de números: "))

#for i in  range(1, n+1): # i varia de 1 a n-1, se n = 3, i de 1 a 3
#    numero = int(input(str(i) + "º número: " ))
 
soma = 0
for i in range(n): #o i assume valores de 0 até n-1
    # print("valor real de i:", i, "valor visivel de i: ", i+1)
    numero = int(input(str(i+1) + "º Numero: "))
    soma = soma + numero
    # print("Soma..........:", soma) # Assim, a soma é visivel
    # para cada numero introduzido

print()
print("Soma..........:", soma) # Assim, a soma aparece apenas 1 vez.
if n == 0:
    media = 0
else:
    media = soma / n

print("A média dos ", n, "números é: ", media)

