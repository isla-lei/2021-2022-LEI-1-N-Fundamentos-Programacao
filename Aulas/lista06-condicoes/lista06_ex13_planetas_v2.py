"""Lista 06-Condições - Exercicio 13.

Escrever um algoritmo que leia um valor representando um determinado peso na Terra e o
número de um planeta da lista anexa e calcule e apresente o valor equivalente desse peso
no planeta escolhido.

Gravidade | Planeta
0.37 | Mercúrio
0.88 |Vénus
0.38 |Marte
2.64 |Júpiter
1.15 |Saturno
1.17 |Urano

Para calcular o peso no planeta usamos a formula:
PesoNoPlaneta = (Pesonaterra/10) * Gravidade
"""
peso_terra = float(input("Peso no Planeta Terra(Kg): "))

print("1. Mercúrio")
print("2. Vénus")
print("3. Marte")
print("4. Júpiter")
print("5. Saturno")
print("6. Urano")

planeta = int(input("Escolha o Planeta {1,6}: "))

if planeta == 1 :
    gravidade = 0.37
    peso_no_planeta = (peso_terra / 10) * gravidade
    print("O seu peso em Mercúrio é: ", peso_no_planeta)
elif planeta == 2:
    gravidade = 0.88
    peso_no_planeta = (peso_terra / 10) * gravidade
    print("O seu peso em Vénus é: ", peso_no_planeta)
elif planeta == 3:
    gravidade = 0.38
    peso_no_planeta = (peso_terra / 10) * gravidade
    print("O seu peso em Marte é: ", peso_no_planeta)
elif planeta == 4:
    gravidade = 2.64
    peso_no_planeta = (peso_terra / 10) * gravidade
    print("O seu peso em Júpiter é: ", peso_no_planeta)
elif planeta == 5:
    gravidade = 1.15
    peso_no_planeta = (peso_terra / 10) * gravidade
    print("O seu peso em Saturno é: ", peso_no_planeta)
elif planeta == 6:
    gravidade = 1.17
    peso_no_planeta = (peso_terra / 10) * gravidade
    print("O seu peso em Urano é: ", peso_no_planeta)
else:
    print("Esse planeta não existe na lista!")

