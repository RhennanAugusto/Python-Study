texto = 'python'

novo_texto = ''
for letra in texto: # eu passo para o for o meu interavel e cada elemento vai passar nesse texto
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto)