from funcao4 import criaListaDeStrings
from funcao6 import criaListaDeListas

def dezMenores(lista):
    maior = lista[0][1]
    novaLista = []
    for li in lista:
        if li[1] <= maior:
            print(li)
            novaLista.insert(0,li)
            maior = li[1]
    return novaLista
            
    #recebe uma lista de cem sublistas que têm a seguinte forma:
    #[string original, número real qualquer], ordene-as do menor
    #para o maior número real, e retorne uma lista com as dez primeiras
    #strings desta lista recém-ordenada.

    #[string original, número real qualquer], ordene-as do menor
    #para o maior número real, e retorne uma lista com as dez primeiras
    #strings desta lista recém-ordenada.
lista = [['00101001', 97.74], ['01010011', 10.05], ['01100110', 95.76], ['10001111', 60.64], ['11010101', 41.72], ['00010011', 61.86], ['01100011', 59.36], ['00010111', 39.83], ['01100010', 23.47], ['00101000', 64.87], ['01010011', 3.2], ['11010001', 32.4]]
print(dezMenores(lista))


# def insertSort(lista, count):
#     for i in range(1, len(lista)):

#         elem = lista[i]

#         pos = i - 1

#         while pos >= 0 and elem < lista[pos]:
#             lista[pos + 1] = lista[pos]
#             pos -= 1
#             count += 1

#         if count > 0:   
#             lista[pos + 1] = elem
#             print(lista)

#     print('Quantidade de alterações:',count)
#     print('Tempo de execucao: ', 2*(count*(count-1))/2)

# count = 0
# insertSort(lista, count)

#https://stackoverflow.com/questions/33000095/how-do-i-sort-data-highest-to-lowest-in-python-from-a-text-file
#https://www.programiz.com/python-programming/methods/list/sort
 