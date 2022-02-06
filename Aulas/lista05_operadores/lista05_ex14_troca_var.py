"""Lista 05-Operadores - Exercicio 14.

Troca de valores entre duas variáveis. 
Escreva um algoritmo que leia dois números colocando-os em variáveis (NumeroA e NumeroB). 
De seguida deve trocar os valores das variáveis, ou seja, 
a variável NumeroA fica com o conteúdo de NumeroB e NumeroB com o conteúdo de NumeroA.
"""

numero_a = int(input("Introduza Numero A...: "))
numero_b = int(input("Introduza Numero B...: "))

print()
print("=====VARIAVEIS ANTES DA TROCA=====")
print("Numero A..:", numero_a)
print("Numero B..:", numero_b)

# versão 1
# com uma terceira variavel
temp = numero_a
numero_a = numero_b
numero_b = temp
print()
print("=====VARIAVEIS DEPOIS DA TROCA=====")
print("Versão 1")
print("Numero A..:", numero_a)
print("Numero B..:", numero_b)

# versão 2
# com somas e subtrações
numero_a = numero_a + numero_b
numero_b = numero_a - numero_b
numero_a = numero_a - numero_b
print()
print("=====VARIAVEIS DEPOIS de NOVA TROCA=====")
print("Versão 2")
print("Numero A..:", numero_a)
print("Numero B..:", numero_b)


# versão 3
# atribuição do python
numero_a, numero_b = numero_b, numero_a
print()
print("=====VARIAVEIS DEPOIS de NOVA TROCA=====")
print("Versão 3")
print("Numero A..:", numero_a)
print("Numero B..:", numero_b)
