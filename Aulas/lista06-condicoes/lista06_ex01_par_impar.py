"""Lista 06-Exercicio 01.

Ler um número e escrever se o número é par ou ímpar.
"""

numero = int(input("Introduza o numero..: "))
resto = numero % 2      # % -> resto da divisão do numero por 2

if resto == 0:
    print("PAR")
else:
    print("IMPAR")

print("FIM")








