import os 

secret_word = 'CBLOL'.lower()
letras_acertadas = ''
numero_tentativas = 0

while True:
    
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1 or not letra_digitada.isalpha():
        print('Digite apenas um caracter alfanumérico.')
        continue

    if letra_digitada in secret_word:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra in secret_word:
        if letra in letras_acertadas:
            palavra_formada += letra
        
        else:
           palavra_formada += '*'
    
    print("Palavra formada:",palavra_formada)

    
    if palavra_formada == secret_word:
        os.system('cls')
        print('Você Ganhou , parabéns')
        print('A palavra era :', secret_word)
        print('Tentativas',numero_tentativas)
        break