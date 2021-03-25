from funcao5 import binarioSeguidoDeReal
from funcao4 import criaListaDeStrings


def criaListaDeListas(listas):
    novaLista = []
    for li in listas:
        novaLista.append(binarioSeguidoDeReal(li))
    return novaLista
    #recebe uma lista de cem strings de zeros e uns e retorna uma nova lista
    #composta por sublistas criadas da seguinte forma:
    #[string original, um número real qualquer].
    #(o número real pode ser gerado aleatoriamente

lista = criaListaDeStrings()
print(criaListaDeListas(lista))

#saida na tela: [['11001100',4.43],['10001000',0.54],...,['01000100',2.12]]
