nome = input(("Qual seu nome ? "))
idade = input(("Qual a sua idade ? "))
espacos = " "


if nome and idade :
    print(f"Seu nome é {nome}")
    print(f"Sua idade é {idade}")
    print(f"Seu nome invertido é :{nome[::-1]}") #para inverter meu nome
    print(f"Seu nome tem {len(nome)} letras")
    if espacos in nome :
        print(f"Seu nome contem espaços")
    else:
        print(f"Seu nome não contem espaços")
    
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")

else:
    print("Voce não digitou nada")


