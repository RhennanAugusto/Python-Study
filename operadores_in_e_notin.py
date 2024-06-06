nome = input('Digite seu nome aqui:')
encontrar = input("Digite o que você deseja encontrar:")

if encontrar in nome :
    print(f'{encontrar} está em nome')

else:
    print(f'{encontrar} não está em nome ')