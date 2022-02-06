"""Lista 06-Condições - Exercicio 10.

Escreva um programa para calcular o IMC – Índice de Massa Corporal.
O IMC é calculado através da seguinte formula:

IMC = peso / (altura ^ 2)

Onde:
    peso é dado em Kg;
    altura é dada em metros.

Seguidamente deve ser dado um diagnostico ao utilizador de acordo com a seguinte tabela:

   IMC         Diagnostico
 < 20            Baixo Peso
 >= 20 até 25    Normal
 >= 25 até 30    Excesso de Peso
 >= 30 até 35    Obesidade
 >= 35           Obesidade Mórbida
"""

peso =  float(input("Introduza o Peso(Kg)...: "))
altura = float(input("Introduza o Altura(m)..: "))

imc = peso / (altura ** 2)

print()
print("O seu IMC....: %0.2f" %imc)

if imc < 20:
    print("Diagnostico..: Baixo Peso")
elif imc < 25: # imc >= 20 and imc < 25
    print("Diagnostico..: Normal")
elif imc < 30: # imc >= 25 and imc < 30
    print("Diagnostico..: Excesso de Peso")
elif imc < 35: # imc >= 30 and imc < 35
    print("Diagnostico..: Obesidade")
else:
    print("Diagnostico..: Obesidade Mórbida")