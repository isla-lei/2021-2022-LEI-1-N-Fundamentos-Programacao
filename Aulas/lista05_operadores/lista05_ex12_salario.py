"""Lista 05-Operadores - Exercicio 12.

Escreva um programa que calcule o salário líquido de um empregado dados:
    Salário bruto;
    Percentagem de desconto de IRS;
    A percentagem de desconto da Segurança Social é 11%.
O programa deve escrever no ecrã o valor do desconto do IRS, o valor do desconto para a Segurança Social e o salário líquido.
"""

salario_bruto =   float(input("Salário Bruto.....: "))
percentagem_irs = float(input("Percentagem IRS...: "))
PERCENTAGEM_SS = 11

valor_irs = salario_bruto * percentagem_irs / 100
valor_ss = salario_bruto * PERCENTAGEM_SS / 100
salario_liquido = salario_bruto - valor_irs - valor_ss

print()
print("IRS...............: ", valor_irs, "€")
print("Segurança Social..: ", valor_ss, "€")
print("Salário Liquido...: ", salario_liquido, "€")

