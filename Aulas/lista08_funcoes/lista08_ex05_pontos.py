"""Lista 08-Procedimentos e Funcoes - Exercicio 5.

Escreva uma FUNÇÃO que receba como PARAMETROS o número de vitórias e o número de empates
de uma equipa de futebol, calcule e RETONRE os pontos tendo em conta que
uma vitoria são 3 pontos e um empate é 1 ponto.
"""

def pontos(num_vitorias, num_empates):
    p = num_vitorias * 3 + num_empates * 1
    return p

    # Fim de função


def calcula_pontos_2(num_vitorias, num_empates):
    return num_vitorias * 3 + num_empates * 1

# programa principal
resultado = pontos(7, 2)

#print("Pontos de 7 vitorias e 2 empates: ", resultado)
print(f"Pontos de 7 vitorias e 2 empates: {resultado}")

# perguntar ao utilizador as vitorias e os empates
vitorias = int(input("Nº de vitorias.: "))
empates = int(input("Nº de empates..: "))

resultado = pontos(vitorias, empates)
print("Pontos de", vitorias, "vitorias e", empates, "empates:", resultado)

print(f"Pontos de {vitorias} vitorias e {empates} empates: {resultado}")
