"""Lista 05-Operadores - Exercicio 6.

O exército português pretende fazer um estudo sobre os gastos de combustível em determinados veículos. 
Elabore um Algoritmo que: leia os litros gastos e os km percorridos por um veículo. 
Calcule os gastos de combustível em €/km e em L/100km.
"""

litros = float(input("Introduza litros gastos.....................: "))
km = float(input("Introduza km percorridos....................: "))
preco = float(input("Introduza o preço por litro do combustivel..: "))

gasto_km = (litros / km) * preco
media100 = (litros / km) * 100
gasto_total = litros * preco

print()
print("Gasto de Euros por Km..: %.2f" %gasto_km, "€")
print("Média aos 100Km........: %.2f" %media100, "litros")
print("Gasto total............: %.2f" %gasto_total, "€")