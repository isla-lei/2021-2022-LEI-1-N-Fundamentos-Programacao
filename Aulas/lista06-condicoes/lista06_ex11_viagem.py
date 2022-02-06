"""Lista 06-Condições - Exercicio 11.

Criar um programa que peça ao utilizador o destino para uma determinada viagem e 
se a viagem é só de Ida ou inclui Volta e calcule e apresente o preço do bilhete de acordo com a seguinte tabela:
Destino	        Ida	    Ida e Volta
Região Norte	25,00€	45,00€
Região Centro	35,00€	65,00€
Região Sul	    45,00€	85,00€
"""

print("Viagem")

print("1 - Regiao Norte")
print("2 - Regiao Centro")
print("3 - Regiao Sul")

destino = int(input("Introduza o seu destino..............: "))
tipo =    int(input("Tipo de viagem: 1. Ida 2. Ida/Volta..: "))

if tipo == 1:
    if  destino == 1:
        print("Preço de viagem: 25€")
    elif destino == 2:
        print("Preço de viagem: 35€")
    elif destino == 3:
        print("Preço de viagem: 45€")
    else:
        print("Dados inválidos!")        
elif tipo == 2:
    if  destino == 1:
            print("Preço de viagem: 45€")
    elif destino == 2:
        print("Preço de viagem: 65€")
    elif destino == 3:
        print("Preço de viagem: 85€")
    else:
        print("Dados inválidos!")        
else:
    print("Dados inválidos!")
