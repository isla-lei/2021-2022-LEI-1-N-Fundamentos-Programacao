"""Lista 08-Procedimentos e Funcoes - Exercicio 1

1. Escreva uma função que receba como parâmetro um número inteiro e retorne -1, 0 ou 1 se este número for negativo, nulo ou positivo, respetivamente
2. Escreva um procedimento que receba como parâmetro um número inteiro e escreva se o número é negativo, nulo ou positivo.
"""

# 1.
def verifica_NNP(numero):
    """ função que recebe um parâmetro de número inteiro e retorna -1, 0 ou 1 se este número for negativo, nulo ou positivo, respetivamente."""

    if numero < 0:
        resultado = -1
    elif numero > 0:
        resultado = 1
    else:
        resultado = 0

    return resultado

    # Fim de função

def verifica_NNP_2(numero):
    """ Função que recebe um parâmetro de número inteiro e retorna -1, 0 ou 1 se este número for negativo, nulo ou positivo, respetivamente."""

    if numero < 0:
        return -1
    elif numero > 0:
        return 1
    else:
        return 0

    # Fim de função


# 2.
def proc_verifica_NNP(numero):
    """Procedimento que recebe como parâmetro um número inteiro e escreva se o número é negativo, nulo ou positivo."""
    if numero < 0:
        resultado = -1
    elif numero > 0:
        resultado = 1
    else:
        resultado = 0

    print(f"Variavel resultado : {res}")

    # Fim procedimento

# Programa Principal
int
num = int(input("Qual o numero...: "))

# invoca função
# criar uma variavel para armazenar o retorno
res = verifica_NNP(num)
print(f"Variavel resultado : {res}")

# ou ...
# escrever diretamente o retorno
print(f"Variavel resultado : {verifica_NNP(num)}")

# invoca o procedimento
proc_verifica_NNP(num)
