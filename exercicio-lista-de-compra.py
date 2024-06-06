lista = []
while True:
    opcao= input("Selecione uma opção\n[i]nserir [a]pagar [l]istar: ")
    
    if opcao == 'inserir':
        produto = input('Produto:')
        lista.append(produto)

    elif opcao == 'listar':
       for indice,nome in enumerate(lista): #aqui posso acessar os valores direto fora da tupla
        print(indice,nome)

    elif opcao == 'apagar':
       opcao2 = int(input("Qual item voce deseja excluir da lista:"))
       if opcao2 < len(lista):
         del lista[opcao2]
       else:
          print('Item não existente')
    
    elif opcao == 'sair':
       print('Programa finalizado com sucesso')
       break
    else :
       print('Opção inválida')