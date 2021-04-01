

def combina(lista):
    listaSubistituta = []
    for i in range(len(lista)):
        l = 1
        print('for l',l)
        print('for i',i)
        print('-----------------')
        while l <= len(lista):
            print('while l',l)
            print('while i',i)
            listaSubistituta.append([lista[i][0],lista[l][0]])
            l += 1
        print('final for ------------------------')
    return listaSubistituta
    #recebe uma lista com dez strings e retorna uma lista de sublistas
    #as sublistas são compostas por duas strings, combinando duas a duas todas as
    #dez strings
    #como combinar:
    #--> pega a primeira string e faz sublistas dela com as outras
    # nove (e vai acrescentando na lista maior). [string1,string2],[string1,string3]...
    #--> pega a segunda string e também, faz sublistas dela com as outras nove, e
    #continua acrescentando na mesma lista maior [string2,string1],[string2,string3]...
    #faz isso com as dez strings
#lista = [['10101010', 93.76], ['00110011', 52.0], ['11111111', 90.4],]
#print(combina(lista))
#saida na tela: [['10101010','11111111'],['10101010','00110011'],... ['11111111','10101010'],...]