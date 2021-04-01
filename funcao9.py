from typing import Type


def muda(string):
    if type(string) is list:
        newList = []
        for values in range(len(string)):
            print(string[values][0])
            string[values][0] = muda(string[values][0])
            print(values)
        return string
    if type(string) is str:
        if string[0] == '1':
            return string.replace('1','0',1)
        if string[0] == '0':
            return string.replace('0','1',1)
        
    #recebe uma string de oito valores zeros ou uns e, **aleatoriamente**,
    #modifique um de seus valores trocando de zero para um ou vice-versa,
    #retornando a string modificada.

#saida na tela: 00110110