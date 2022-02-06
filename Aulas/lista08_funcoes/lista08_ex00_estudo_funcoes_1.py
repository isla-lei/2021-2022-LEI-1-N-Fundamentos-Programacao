'''

Elaborar um programa que pede ao utilizador os seguintes anos:
- Ano Nascimento
- Ano Entrada na Escola
- Ano Atual
- Ano da Revolução de 25 Abril
E esccreva se o ano é bissexto ou não bissexto
'''

# Programa SEM FUNÇÕES

# Ano Nascimento
ano_nascimento = int(input("Ano Nascimento.........: "))
if ((ano_nascimento % 4 == 0 and ano_nascimento % 100 != 0) or (ano_nascimento % 100 == 0 and ano_nascimento % 400 == 0)):
    print(ano_nascimento, "- Bissexto")
else:
    print(ano_nascimento, "- Não Bissexto")

# Ano Entrada na Escola
ano_entrada_escola = int(input("Ano Entrada na Escola..: "))
if ((ano_entrada_escola % 4 == 0 and ano_entrada_escola % 100 != 0) or (ano_entrada_escola % 100 == 0 and ano_entrada_escola % 400 == 0)):
    print(ano_entrada_escola, "- Bissexto")
else:
    print(ano_entrada_escola, "- Não Bissexto")

# Ano Atua
ano_atual = int(input("Ano Atual..............: "))
if ((ano_atual % 4 == 0 and ano_atual % 100 != 0) or (ano_atual % 100 == 0 and ano_atual % 400 == 0)):
    print(ano_atual, "- Bissexto")
else:
    print(ano_atual, "- Não Bissexto")

# Ano Revolução de 25 Abril
ano_revolucao = int(input("Ano Revolução de 25 Abril.: "))
if ((ano_revolucao % 4 == 0 and ano_revolucao % 100 != 0) or (ano_revolucao % 100 == 0 and ano_revolucao % 400 == 0)):
    print(ano_revolucao, "- Bissexto")
else:
    print(ano_revolucao, "- Não Bissexto")
