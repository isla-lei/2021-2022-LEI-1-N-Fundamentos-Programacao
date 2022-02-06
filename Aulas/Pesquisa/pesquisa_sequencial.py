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

# programa principal
# testar a função

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




