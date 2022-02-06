"""Lista 05-Operadores - Exercicio 3.

Calcular o volume de uma circunferência dado o seu raio.
Volume = 4/3.Pi.Raio^3   
"""

raio = float(input("Introduza o raio: "))
PI = 3.1415

volume = 4/3 * PI * raio ** 3

print("Volume: ", volume)

#formatar casas decimais (2)
print("Volume: %.2f" %volume)