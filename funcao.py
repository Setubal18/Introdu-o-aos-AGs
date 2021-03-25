def converteBinarioReal(string):
    if(len(string)==8):
        return float(f'{int(string[:2], 2)}.{int(string[3::], 2)}')
    else:
        raise Exception('Número menor ou maior que o permitido')

    #recebe uma string com oito valores 'zero' ou 'um' sendo os dois primeiros
    #equivalentes à parte inteira e os seis restantes equivalente à parte
    #fracionária de um número binário.
    #A função deverá retornar este número convertido para um número real (float)

#print(converteBinarioReal('11001100'))
# saida na tela: 3.12