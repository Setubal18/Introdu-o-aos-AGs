def converteRealBinario(numero):
    string = str(numero)
    binario = ''
    reais = string.split('.')
    bina = f'{bin(int(reais[0]))}'+ f'{bin(int(reais[1]))}'
    binsLista = bina.split('b')
    for i in binsLista: binario += i
    return binario
    #recebe um valor real (float) e converte para binário fracionário
    #no formato de uma string com oito valores zero ou um, sendo
    #os dois primeiros equivalentes à parte inteira e os seis restantes
    #equivalente à parte fracionária do número binário.
    #A função deve retornar esta string.

#print(converteRealBinario(3.12))
