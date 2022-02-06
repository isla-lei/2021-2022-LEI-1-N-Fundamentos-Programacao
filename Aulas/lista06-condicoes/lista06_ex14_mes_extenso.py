"""Lista 06-Condições - Exercicio 14.

Programa para converter um número literal representando um mês no seu correspondente mês por extenso. 
Portanto, ler um número inteiro entre 1 e 12 e escrever o mês respectivo por extenso. 
Caso o utilizador digite um número fora desse intervalo, deverá aparecer uma mensagem informando 
que não existe mês com esse número.
	Exemplo: Mês: 11 
	Resposta : Novembro
"""

mes_numerico = int(input("Numero do Mês...: "))

if mes_numerico == 1:
    mes_extenso = "Janeiro"
elif mes_numerico == 2:
    mes_extenso = "Fevereiro"
elif mes_numerico == 3:
    mes_extenso = "Março"
elif mes_numerico == 4:
    mes_extenso = "Abril"
elif mes_numerico == 5:
    mes_extenso = "Maio"
elif mes_numerico == 6:
    mes_extenso = "Junho"
elif mes_numerico == 7:
    mes_extenso = "Julho"
elif mes_numerico == 8:
    mes_extenso = "Agosto"
elif mes_numerico == 9:
    mes_extenso = "Setembro"
elif mes_numerico == 10:
    mes_extenso = "Outubro"
elif mes_numerico == 11:
    mes_extenso = "Novembro"
elif mes_numerico == 12:
    mes_extenso = "Dezembro"
else:
    mes_extenso = "Mês inválido!"

print(mes_extenso)




