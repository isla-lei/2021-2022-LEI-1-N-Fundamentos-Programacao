"""Lista 06-Condições - Exercicio 3.

Ler um número e calcular o seu módulo.
|z| = -z se z < 0
0 se z = 0
z se z>0
"""

numero = int(input("Introduza o número..: "))

if numero < 0: 
    print("Módulo do numero: ", numero * - 1)
else:
    print("Módulo do numero: ", numero)

