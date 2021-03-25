from funcao3 import criaString
def criaListaDeStrings():
    random = []
    for i in range(99):
        random.append(criaString())
    return random
    #cria uma lista com cem strings, cada string composta por
    #oito valores zero ou um (podem ser criadas aleatoriamente),
    #retornando-a

#print(criaListaDeStrings())
#saida na tela: ['10101101','10110101','01101010',...,'10101010']
