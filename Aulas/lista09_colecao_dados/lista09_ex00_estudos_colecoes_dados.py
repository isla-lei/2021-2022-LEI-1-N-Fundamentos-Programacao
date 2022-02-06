"""Lista 09-Colecoes - Estudo de coleções de dados.

Estudo de coleções de dados:
-list
-tuple
-set
-dictionary
"""

# LIST - Coleção ordenada, alterável e que permite valores duplicados
# []

lista_numeros =[0]*6 # define uma lista com 6 celulas com o valor 0
print(lista_numeros)
lista_numeros[0] = 10
lista_numeros[1] = 20
lista_numeros[2] = 30
lista_numeros[3] = 40
lista_numeros[4] = 50
lista_numeros[5] = 60
print(lista_numeros)

###
celulas = int(input("Quantidade de celulas: "))
lista_dados = [0]*celulas
print("Lista criada: ", lista_dados)
###

###
print("Introduzir numa lista 5 numeros")
tam = 5
lista_numeros = []
for i in range(tam):
    numero = int(input(str(i+1) + "º Número: "))
    lista_numeros.append(numero)

print("Lista: ", lista_numeros)
###

###
# loop atraves dos elementos
print("Lista")
for elemento in lista_numeros:
    print(elemento)

# loop atraves do indice
print()
print("Lista")
for i in range(len(lista_numeros)):
    print(lista_numeros[i])
###

###
#Lista de listas
lista_notas = []
while True:
    numero = int(input("Numero (zero p/ terminar): "))

    if numero == 0:
        break

    nome = input("Nome: ")
    nota = float(input("Nota:"))
    registo = [numero, nome, nota]

    lista_notas.append(registo)

print("Lista notas: ", lista_notas)
# loop atraves dos elementos
print("Lista de notas")
for elemento in lista_notas:
    print(elemento)
###
