entrada = input("Digite [E] para entrar ou [S] para sair:")
senha_digitada = input("Digite a senha :")
senha_permitida = ("123456")

if (entrada == 'E' or entrada =='e') and senha_digitada == senha_permitida :
          print("Entrada efetuada com sucesso ")

if (entrada == 'S' or entrada =='s') and senha_digitada == senha_permitida:
            print('sair')

else : 
        print("Algo de errado aconteceu tente mais tarde")
           
