def cruzaUm(stringA,stringB):
    novaStringA = stringA[:4] + stringB[4::]
    novaStringB = stringB[:4] + stringA[4::]
    return [novaStringA,novaStringB]
    #recebe duas strings de oito valores zeros ou uns e cria
    #duas novas strings no seguinte formato:
    #-->uma string será composta pelos quatro primeiros valores da primeira
    #seguidos pelos quatro últimos da segunda;
    #-->e a outra string será composta pelos quatro primeiros valores da segunda
    #string seguidos pelos quatro últimos da primeira string.
    #retorna as duas strings em uma lista

#print(cruzaUm('10110100','11001000'))
#saida na tela: ['10111000','11000100']
