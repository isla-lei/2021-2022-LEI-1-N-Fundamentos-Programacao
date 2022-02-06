"""Lista 05-Operadores - Exercicio 2.

Ler um determinado valor em Km e converter para Pés, Milhas Náuticas, e Milhas
   
    1 Pé 	= 0,304 m
    1 MN 	= 1852 m
    1 M 	= 1609 m
"""

km = float(input("Introduza valor em km: "))

km_metros = km * 1000

pes = km_metros / 0.304
mn = km_metros / 1852
m = km_metros / 1609

print(pes,  " Pés")
print(mn, " Milhas náuticas")
print(m, " Milhas")

# formatações
print("{:.2f}".format(pes) + " Pés")
print("{:.2f}".format(mn) + " Milhas náuticas")
print("{:.2f}".format(m) + " Milhas")

#ou
#print("Milhas náuticas %.2f" % mn)
