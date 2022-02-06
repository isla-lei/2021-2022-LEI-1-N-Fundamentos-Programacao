"""Lista 05-Operadores - Exercicio 4.

Ler a área de uma circunferência e calcular o seu perímetro  
    area = PI.R^2
    perimetro = 2.PI.R
    raio = raiz(area/PI)
"""
import math

area = float(input("Introduza a area: "))

PI = 3.1415
raio = math.sqrt(area/PI)
perimetro = 2 * PI * raio

print("Perímetro: %.2f " %perimetro)


