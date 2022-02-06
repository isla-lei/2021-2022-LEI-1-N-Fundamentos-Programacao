"""Lista 05-Operadores - Exercicio 11.

Escreva um programa que leia uma temperatura em 0F (graus Fahrenheit) e transforme em 0C (Graus célsius)
    C = 5 (F - 32) / 9   
"""

graus_far = float(input("Temperatura em graus Fahrenheit..: "))
graus_cel = 5 * (graus_far - 32) / 9

print("Temperatura em graus Célsius: %.2f" %graus_cel)