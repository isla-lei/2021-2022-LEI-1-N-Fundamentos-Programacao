"""Lista 05-Operadores - Exercicio 1.

Ler dois números inteiros a partir do teclado e calcular e escrever no ecrã a sua soma, produto e média
"""

op1 = input("Introduza operador 1: ")
op2 = input("Introduza operador 2: ")

soma = int(op1) + int(op2)
produto = int(op1) * int(op2)
media = soma / 2

print('Soma....: ', soma)
print('Produto.: ', produto)
print('Media...: ', media)

#ou..
#print('Soma....: ' + str(soma))
#print('Produto.: ' + str(produto))
#print('Media...: ' + str(media))
