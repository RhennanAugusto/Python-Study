while True:
    numeroperguntado = input("Digite o numero desejado aqui e caso deseje parar o codigo , digite sair:")
    
    if numeroperguntado.lower() == "sair":
           print("Codigo finalizado")
           break  # se não usar o break aqui ele escapa pro except tambem 
    
    try :
       if  numeroperguntado.isdigit():
         numero = int(numeroperguntado)      
         if  numero % 2 ==  0 : # aqui eu uso o % (resto da divisao) nesse caso por 2 é 0 para definir se é par
           print(f"O Numero {numero} é par")
         else :
           print(f"O numero {numero} não é par")
       else:
           raise ValueError ("Você não digitou um numero valido,tente novamente")
    
    except ValueError as e:
         print("Tipo de exceção" , type(e))
         print("Mensagem de erro : ", e)
