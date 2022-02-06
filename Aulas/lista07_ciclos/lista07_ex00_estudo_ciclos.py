"""Estudo dos ciclos (loops)

Estudo dos ciclos:
-while
-for
"""

# Escrever os numeros de 10 a 30
num = 10
while num <=30:
    print(num)
    num = num + 1

print("FIM")

# Pedir numeros ao utilizador até que introduza o zero
# pedir numeros enquanto o numero (var) seja diferente de zero

# numero = int(input("Numero inicial: "))
# ou ..
numero = -1 # codigo-> garantir que entra no ciclo
contador = 1
while numero !=0:
    numero = int(input("Numero " + str(contador) + ": "))
    contador = contador + 1 # contador =+1
    
    
# OU ...
contador = 1
while True: # criar um loop infinito, temos que definir criterio de termino
    numero = int(input("Numero " + str(contador) + ": "))
      

    # definir criterio de termino
    if numero == 0:
        break # termina o ciclo

    contador = contador + 1 # contador =+1

contador = contador - 1
print(f"quantidade de numeros: {contador} ")


# Validar uma nota enter 0 e 20
# Tecnica: fazer a pergunta da nota (repetir), 
# até que o utilizador introduza uma nota valida

while True:
    nota = float(input("Introduz nota [0..20]: "))

    # criterio de terminação
    if nota >=0 and nota <= 20:
        break # termina loop
    else:
        print(" Nota inválida!")

print("Nota aceite: ", nota)



"""
Ciclo FOR
"""
# escreve os numeros de 10 a 30
for num in range(10, 31): # a var num assume valores entre 10 e 30
    print(num)

# equivalente com while
num = 10
while num <=30:
    #print(num)
    num = num + 1

print("i de 0 a 4")
for i in range(5): # i de 0 a 4
    print(i)

print("i de 1 a 4")
for i in range(1, 5): # i de 1 a 4
    print(i) 

print("i de 1 a 4 de 2 em dois")
for i in range(1, 5, 2): # i de 1 a 4
    print(i) 

# escrever n numeros
n = int(input("Quantidade de numeros: "))
for i in range(1, n+1):
    print(i)