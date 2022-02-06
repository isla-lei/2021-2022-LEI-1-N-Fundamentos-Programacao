"""Lista 07-Ciclos - Exercico 2.

Altere o programa AnoBissexto para que de forma automática
forneça uma lista de anos com a respectiva classificação
quanto a ser bissexto ou não.
Assim, o programa deve pedir qual o período em anos a ser avaliado.
"""

ano_inicial = int(input("Ano inicial..: "))
ano_final = int(input("Ano final....: "))

for ano in range(ano_inicial, ano_final + 1):
    if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 100 == 0 and ano % 400 == 0)):
        print(ano, "- BISSEXTO")
    else:
        print(ano, "- Não Bissexto")


