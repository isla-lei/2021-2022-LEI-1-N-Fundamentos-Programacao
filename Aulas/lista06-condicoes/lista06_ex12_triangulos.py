"""Lista 06-Condições - Exercicio 12.

Ler o cumprimento dos três lados de um triângulo, apresentar a classificação para esse triângulo, de acordo com o seguinte:
	Três lados iguais		- equilátero
	Dois lados iguais		- isósceles
	Três lados diferentes	- escaleno

"""

lado1 = int(input("1º lado do triangulo.....: "))
lado2 = int(input("2º lado do triangulo.....: "))
lado3 = int(input("3º lado do triangulo.....: "))

if lado1 == lado2 and  lado2 == lado3:
    print("Triangulo Equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Triangulo Isósceles")
else:
    print("Triangulo Escaleno")

