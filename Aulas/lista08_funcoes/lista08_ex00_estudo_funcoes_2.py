'''

Elaborar um programa que pede ao utilizador os seguintes anos:
- Ano Nascimento
- Ano Entrada na Escola
- Ano Atual
- Ano da Revolução de 25 Abril
E esccreva se o ano é bissexto ou não bissexto
'''

# Programa COM FUNÇÕES

def verifica_bissexto(ano):
    """Função (Procedimento) que recebe como parametro um ano e escreve se é bissexto ou não."""
    if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 100 == 0 and ano % 400 == 0)):
        print(ano, "- Bissexto")
    else:
        print(ano, "- Não Bissexto")
    # fim da função


# PROGRAMA PRINCIPAL
# Ano Nascimento
ano_nascimento = int(input("Ano Nascimento............: "))
verifica_bissexto(ano_nascimento)

# Ano Entrada na Escola
ano_entrada_escola = int(input("Ano Entrada na Escola.....: "))
verifica_bissexto(ano_entrada_escola)

# Ano Atua
ano_atual = int(input("Ano Atual.................: "))
verifica_bissexto(ano_atual)

# Ano Revolução de 25 Abril
ano_revolucao = int(input("Ano Revolução de 25 Abril.: "))
verifica_bissexto(ano_revolucao)

# outro ano
verifica_bissexto(2021)

