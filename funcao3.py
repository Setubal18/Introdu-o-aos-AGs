from random import randint
def criaString():
    size = 0
    string=''
    while size < 8:
        string += f'{randint(0,1)}'
        size +=1
    return string

    
    #cria uma string com oito valores aleatórios zeros ou uns, retornando-a

#print(criaString())
#saida na tela: 11001100
