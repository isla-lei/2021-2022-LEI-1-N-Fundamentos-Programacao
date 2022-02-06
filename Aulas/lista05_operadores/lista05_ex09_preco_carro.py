"""Lista 05-Operadores - Exercicio 9.

Escreva um algoritmo que calcule o preço final de um carro para o consumidor, os valores pagos de impostos 
e o lucro do distribuidor, sabendo o custo de fábrica do carro e que são pagos os seguintes impostos: 
    a) IA : 30% sobre o custo do carro; 
    b) IVA: 23 % sobre o custo do carro já com IA;
    c) lucro do distribuidor: 12% sobre o custo do carro.
"""

custo_inicial = float(input("Custo de Fábrica do Carro:.. "))

VALOR_IA = 30 / 100
VALOR_IVA = 23 / 100
VALOR_LUCRO = 12 / 100

ia = custo_inicial * VALOR_IA 
iva = (custo_inicial + ia) * VALOR_IVA 
lucro_vendedor = custo_inicial * VALOR_LUCRO

total_impostos = ia + iva
preco_final = custo_inicial + total_impostos + lucro_vendedor

print()
print("IA..................: ", ia)
print("IVA.................: ", iva)
print("Total Impostos......: ", total_impostos)
print("Lucro Distribuidor..: ", lucro_vendedor)
print("Preço Final.........: ", preco_final)