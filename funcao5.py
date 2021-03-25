from random import SystemRandom, randint

def binarioSeguidoDeReal(string):
    if(len(string)==8):
        secure_random = SystemRandom()
        randomfloat = secure_random.random()
        return [string, float(f'{randint(0,99) + round(randomfloat, 2)}')]
    else:
        raise Exception('Número menor ou maior que o permitido')


#print(binarioSeguidoDeReal('11001100'))