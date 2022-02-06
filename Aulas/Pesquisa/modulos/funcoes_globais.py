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

    
