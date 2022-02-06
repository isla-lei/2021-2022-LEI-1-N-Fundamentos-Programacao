"""Lista 06-Exercicio 07.

Desenvolva um algoritmo que:
Leia um número representando um determinado ano. Descobrir se esse número 
(ano) representa um ano bissexto. Um ano é bissexto se cumprir a 
seguintes condições:
(1) se for divisível por 4,
(2) se não for divisível por 100.
Há uma excepção a esta última regra:
(3) no caso de ser divisível por 100, será bissexto se for divisível por
400.
Exemplos:
1980 – bissexto – regras 1 e 2
1900 – não bissexto – regras 1 e 2
2000 – bissexto – regras 1 e 3
2002 – não bissexto – regra 1
"""

ano = int(input("Introduza o ano...: "))

if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(" ANO -  B I S S E X T O")
    num_dias = 366
else:
    print(" NÃO É ANO BISSEXTO")
    num_dias = 365

#print("Este ano tem ", num_dias, "dias")
#outra forma
print(f"Este ano tem {num_dias} dias")
print(" FIM ")
