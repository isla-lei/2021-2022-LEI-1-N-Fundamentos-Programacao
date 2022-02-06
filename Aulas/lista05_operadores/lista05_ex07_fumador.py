"""Lista 05-Operadores - Exercicio 7.

Calcular a quantidade de dinheiro gasto por um fumador. 
Dados: o número de anos que ele fuma, o n.º de cigarros fumados por dia e o preço o maço de cigarros.
Obs: cada maço de cigarros tem 20 unidades
"""

anos_fuma = float(input("Fuma há quantos anos.................: "))
cigarros_dia = float(input("Quantos cigarros fuma por dia........: "))
preco_maco = float(input("Quanto custa cada maço de cigarros...: "))

cigarros_vida = cigarros_dia * 365 * anos_fuma
gasto_total = cigarros_vida / 20 * preco_maco

print()
print("Total Dinheiro Gasto.................: %.2f" %gasto_total, "€")