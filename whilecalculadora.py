while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite o outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    numero_1_float = 0 # caso essa variavel fique apenas dentro do bloco e a gente tentar usar fora pode dar problema
    numero_2_float = 0
    

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True 

    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos dos numeros digitados, são inválidos.")
        continue # para voltar ao topo do laço
    
    operadores_permitidos ='+-/*'

    if operador not in operadores_permitidos :
        print("Operador inválido")
        continue

    if len(operador)> 1:
        print("Digite apenas um operador.")
        continue
    
    print('Realizando sua operação. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float}=',numero_1_float + numero_2_float)
    
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float}=', numero_1_float - numero_2_float)

    elif operador == '/':
        print(f'{numero_1_float} / {numero_2_float}=',numero_1_float / numero_2_float)
    
    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float}=',numero_1_float * numero_2_float)

    else:
        print('Nunca deveria chegar aqui')
    
    saida = input("Deseja sair da calculadora ? [s]im :").lower().startswith('s')
    if saida is True:
        print('Saiu da calculadora com sucesso !!!')
        break
