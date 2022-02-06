# importar a função "pesquisa_valor"  do modulo "funcoes_globais.py"
from funcoes_globais import pesquisa_valor, conta_valores
# usar: pos = pesquisa_valor(nomes, nome_pesquisar)


# programa principal
# testar a função

# listas
nomes = ["Martim", "Jose", "Pedro", "Teresa", "Nádia"]
notas = [15, 10, 8, 15, 11]

print(nomes)
print(notas)

nome_pesquisar = input("Nome a pesquisar: ")
pos = pesquisa_valor(nomes, nome_pesquisar)
if pos == -1:
    print(f"O nome {nome_pesquisar} não existe na lista!")
else:
    print(f"A nota do nome {nome_pesquisar} é: {notas[pos]}")

nota_pesquisar = int(input("Nota a pesquisar (1ª ocorrencia): "))
pos = pesquisa_valor(notas, nota_pesquisar)
if pos == -1:
    print(f"A nota {nota_pesquisar} não existe na lista!")
else:
    print(f"O nome da nota {nota_pesquisar} é: {nomes[pos]}")


# testar a função conta_valores
nome_pesquisar = input("Nome a contar:")
conta = conta_valores(nomes, nome_pesquisar)
print(f"O nome {nome_pesquisar} existe {conta} vezes na lista")

nota_pesquisar = int(input("Nota a contar: "))
conta = conta_valores(notas, nota_pesquisar)
print(f"A nota {nota_pesquisar} existe {conta} vezes na lista")


