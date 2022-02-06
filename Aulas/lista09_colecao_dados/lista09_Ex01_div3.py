"""
Construa um programa que leia do utilizador uma sequência 
de 10 números inteiros, e escreva primeiro os valores 
que são divisíveis por 3 e depois os valores 
que não são divisíveis por 3.
deve usar uma lista de Python
"""

lista_numeros = [] # lista vazia
for i in range(5): # i de 0 a 9

    numero = int(input(str(i+1) + "º Numero: "))

    # colocar o numero na lista
    lista_numeros.append(numero)


# percorrer a lista "lista_numeros" e verificar se
# cada elemento é div 3

print("DIV 3")
print("=====")
# percorrer atraves do indice
comprimento = len(lista_numeros)
for i in range(comprimento):
    if lista_numeros[i] % 3 == 0:
        print(lista_numeros[i])


print("NÃO DIV 3")
print("=========")
# percorrer atraves do indice
for i in range(comprimento):
    if lista_numeros[i] % 3 != 0:
        print(lista_numeros[i])

        