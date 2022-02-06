"""Lista 06-Condições - Exercicio 2.

Ler dois números A, B e calcular a soma dos números pares e o produto dos números ímpares.
No caso de não serem os dois da mesma natureza (par ou impar) deve aparecer ao utilizador a mensagem.
"""

numero_a = int(input("Introduza o número A..: "))
numero_b = int(input("Introduza o número B..: "))

if numero_a % 2 == 0 and numero_b % 2 == 0: 
    print("A soma dos numeros é: ", numero_a + numero_b)
elif numero_a % 2 != 0 and numero_b % 2 != 0: 
    print("O produto dos numeros é:", numero_a * numero_b)
else:
    print("O numeros não são da mesma natureza!")

