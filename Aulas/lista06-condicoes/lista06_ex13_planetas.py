"""Lista 06-Condições - Exercicio 13.

Escrever um algoritmo que leia um valor representando um dedeterminado
peso na Terra e o número de um planeta da lista anexa e
calcule e apresente o valor equivalente desse peso no planeta escolhido.
Para calcular o peso no planeta usamos a formula:

PesoNoPlaneta = PesoNaTerra / 10 * Gravidade

#  Planeta        Gravidade
1   Mercúrio        0.37
2   Vénus           0.88
3   Marte           0.38
4   Júpiter         2.64
5   Saturno         1.15
6   Urano           1.17

"""

peso_na_terra = float(input("Qual o seu peso na Terra (Kg).: "))

print("PLANETAS")
print("1. Mercúrio")
print("2. Vénus")
print("3. Marte")
print("4. Júpiter")
print("5. Saturno")
print("6. Urano")

planeta = int(input("Escolha o planeta (1..6)..: "))

if planeta == 1:
    #peso_no_planeta = (peso_na_terra / 10) * 0.37
    gravidade = 0.37
elif planeta == 2:
    gravidade = 0.88
elif planeta == 3:
    gravidade = 0.38
elif planeta == 4:
    gravidade = 2.64
elif planeta == 5:
    gravidade = 1.15
elif planeta == 6:
    gravidade = 1.17
else:
    print("Planeta errado!")

if planeta >= 1 and planeta <= 6:
    peso_no_planeta = (peso_na_terra / 10) * gravidade
    print("O seu peso no planeta escolhido é: ", peso_no_planeta)