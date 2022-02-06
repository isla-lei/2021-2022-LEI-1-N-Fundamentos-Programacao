# listas
nomes = ["Martim", "Jose", "Pedro", "Teresa", "Nádia"]
notas = [15, 10, 8, 15, 11]

print(nomes)
print(notas)

# função
def pesquisa_valor(lista, termo_pesquisar):
    # pesquisar o termo_pesquisar em toda a lista
    # percorrer toda a lista, e retorna a posicao 
    # desse termo_pesquisa na lista
    # por ex: 
    # -se o termo_pesquisar = "Pedro"
    # -retorna posicao = 2

    for posicao in range(len(lista)): # poiscao de 0 a tam lista -1
        if lista[posicao] == termo_pesquisar:
            return posicao # retorna e termina pesquisa

    # termo_pesquisar não existe na lista
    return -1 

# Função (conta_valores), que recebe uma lista e
# o termo a pesquisar, e conta e retorna o nº de ocorrencias
# desse termo na lista
def conta_valores(lista, termo_pesquisar):
    
    conta = 0
    for i in range(len(lista)): # poiscao de 0 a tam lista -1
        if lista[i] == termo_pesquisar:
            conta = conta + 1 # conta +=1

    return conta


# programa principal
# testar a função pesquisa_valor


nome_pesquisar = input("Nome a pesquisar:")
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

