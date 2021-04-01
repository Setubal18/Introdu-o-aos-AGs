def cruzaDois(stringA,stringB):
        novaStringA = stringA[:2] + stringB[2:6] + stringA[6::]
        novaStringB = stringB[:2] + stringA[2:6] + stringB[6::]
        return [novaStringA,novaStringB]
    #recebe duas strings de oito valores zeros ou uns e cria
    #duas novas strings no seguinte formato:
    #-->uma string será composta pelos dois primeiros valores da primeira seguidos
    #pelos quatro do meio da segunda e pelos dois últimos da primeira;
    #-->e a outra string será composta pelos dois primeiros valores da segunda string
    #seguidos pelos quatro do meio da primeira e pelos dois últimos da segunda string

print(cruzaDois('10110100','11001000'))
#saida na tela: ['10001000','11110100']