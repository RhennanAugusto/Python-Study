frase = 'O Python é uma linguagem de programação '\
        'multiparadigma '\
        'Python foi criado por Guido Van Rossum.'.lower()

frase_sem_espacos = frase.replace(' ','')

letra_mais_comum = ''
quantidade_letra_mais_comum = 0
i = 0 

while i < len (frase_sem_espacos):
    letra_atual = frase_sem_espacos [i]
    quantas_vezes_letra = frase_sem_espacos.count(letra_atual)
    
    if quantas_vezes_letra > quantidade_letra_mais_comum:
        letra_mais_comum = letra_atual
        quantidade_letra_mais_comum = quantas_vezes_letra

    #print(letra_atual,quantas_vezes_letra)
    i += 1
    
print(f'A letra que mais aparece nesse caso é "{letra_mais_comum}" que apareceu {quantidade_letra_mais_comum}x')







