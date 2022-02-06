"""Lista 06-Condições - Exercicio 4.

Ler a unidade (Esc ou Euros) e um valor expresso na unidade, calcular o valor convertido na outra unidade.
"""

unidade = int(input("Unidade (1. Esc ou 2. Euros)..: "))
valor = float(input("Introduza o valor.............: "))

if unidade == 1:
   # converter para euros
   conversao = valor / 200.482
   print( valor, "Escudos equivale a ", conversao, "€")
else:
   conversao = valor * 200.482
   print( valor, "Euros equivale a ", conversao, "$(Esc)")



