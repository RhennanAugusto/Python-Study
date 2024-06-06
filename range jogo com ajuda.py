secret_word = 'One Piece'.lower()
guessed_letters = [] # lista de letras tentadas
display_word = ['*' if char.isalpha() else char for char in secret_word]

while True:
    print('Palavra:',''.join(display_word))
    user_try = input("Digite apenas uma letra: ")

    if len(user_try) > 1 :
        print('Você não digitou apenas uma letra , tente novamente.')
        continue
    
    elif not user_try.isalpha():
        print('Números não são válidos, tente novamente')
        continue
    
    elif user_try in guessed_letters:
            print('Voce ja tentou essa letra,tente outra')
            continue
    
    guessed_letters.append(user_try)

    if user_try in secret_word:
         for i in range(len(secret_word)):
              if secret_word[i] == user_try:
                   display_word[i] = secret_word[i]
    
    else:
         print('Essa letra não está na palavra secreta')

    if '*' not in display_word:
         print('Parabens !!! voce adivinhou a palavra secreta:', ''.join(display_word))
         break

