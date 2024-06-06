valor = 'Valor qualquer'

i = 0
while i < len (valor):
    letra = valor[i]
    
    if letra == ' ':
        break # caso tenha um break aqui o else não vai ser executado

    print(letra)
    i += 1

else:
    print('Não foi encontrado espaço na string.')

print('fora do while')