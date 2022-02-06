"""Lista 05-Operadores - Exercicio 13.

Pretende-se um programa que leia do teclado as notas (0 a 20 valores) obtidas por um aluno de programação 
nas componentes de nota de teste e nota de trabalho.
Depois o programa deve calcular a sua média ponderada e escrever a nota final no ecrã.
O peso (%) do teste deve ser pedida ao utilizador e o peso do trabalho deve ser calculado.
"""

#ler a nota e converter para Float (numero com casas decimais)
nota_teste = float(input("Introduza a nota do teste....: "))
nota_trabalho = float(input("Introduza a nota do trabalho.: "))
percentagem_teste = float(input("Introduza o peso (%) do teste: "))
percentagem_trabalho = 100 - percentagem_teste

#print(type(nota_teste))
#print(type(nota_trabalho))

valor_nota_teste = nota_teste * (percentagem_teste / 100)
valor_nota_trabalho = nota_trabalho * (percentagem_trabalho / 100)
nota_final = valor_nota_teste + valor_nota_trabalho

print()
print("Peso (%) do Teste............: ", percentagem_teste, "%")
print("Valor Nota Teste.............: ", valor_nota_teste)
print()
print("Peso (%) do Trabalho.........: ", percentagem_trabalho, "%")
print("Valor Nota Trabalho..........: ", valor_nota_trabalho)
print()
print("Nota Final...................: ", nota_final)







