""""
Segundo uma tabela médica, o peso ideal está relacionado com a altura e sexo. Criar um 
programa que receba a altura e o sexo de uma pessoa, calcular e apresentar o peso ideal, 
utilizado as seguinte formulas:
▪ Homens: (72.7 * Altura) - 58
▪ Mulheres: (62.1 * Altura) - 44.7
"""
altura = float(input("Introduza a altura: "))
sexo = input("Qual o genéro ? Indroduza M/m para masculino ou F/f para feminino ? ")

if (sexo == 'm' or sexo == 'M'):
    print("O seu peso ideal é", (72.5 * altura) - 58, "Kg")
elif (sexo == 'f' or sexo == 'F'):
    print("O seu peso ideal é", (62.1 * altura) - 44.7, "Kg")
else: 
    print("Genero inválido!")
