

#%%
#Por mais que nao seja um conteudo de Algoritimos geneticos, vou adicionar redes neurais temporariamente aqui, futuramente colocarei em seu proprio repo
from colorama import Fore

def calculaerro(valor1,valor2):
    return valor1-valor2

def somaponderada(**kwargs):
    return (kwargs["valor1"] * kwargs["peso1"]  + (kwargs["valor2"] * kwargs["peso2"])) + kwargs["bias"]

def limiar(valor):
    if (valor >= 0):
        return 1
    else:
        return 0

def atualizaPeso(**kwargs):
    peso1 = kwargs["peso1"] + (kwargs["error"] * kwargs["valor1"])
    peso2 = kwargs["peso2"] + (kwargs["error"] * kwargs["valor2"])
    bias = kwargs["bias"] + kwargs["error"]
    return [peso1,peso2,bias]

valores1 = [2,-2,-2,-1]
valores2 = [2,-2,2,1]
objetivos = [0,1,0,1]
pesos = [0,0,0]
flag = True
cont = 0
while flag:
    ondeEsta = []
    for num in range(4):

        print('\n')
        print(f'{Fore.LIGHTBLACK_EX}' f'____{num}____')

        resultado = somaponderada(
            valor1=valores1[num],
            peso1=pesos[0],
            valor2=valores2[num],
            peso2=pesos[1],
            bias=pesos[2])

        print(f'{Fore.CYAN}' f'O resultado é : {resultado}')
        resultado = limiar(resultado)
        ondeEsta.append(resultado)
        print(f'{Fore.CYAN}' f'O resultado da limiar é : {resultado}')
        error = calculaerro(objetivos[num],resultado)
        print(f'{Fore.RED}' f'O erro é : {error}')

        if(error != 0 ):
            pesos = atualizaPeso(
            valor1=valores1[num],
            peso1=pesos[0],
            valor2=valores2[num],
            peso2=pesos[1],
            bias=pesos[2],
            error=error)
            print(f'{Fore.GREEN}' f'Novos pesos: {pesos}')
            flag = True
        else:
            print(f'{Fore.YELLOW}' f'Pesos: {pesos}')
            flag = False
        print(f'{Fore.LIGHTBLACK_EX}' '______________')
    cont +=1
    print('\n')
    print(f'{Fore.MAGENTA}' f'NUMERO DE RODADAS {cont}')
    print(f'Onde estou no Objetivos : {ondeEsta}')
    print(f'Peso final : {pesos}')

# %%
