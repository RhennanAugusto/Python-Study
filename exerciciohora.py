while True : 
      
      entrada = input("Digite a hora em numeros inteiros :")

      if entrada.lower() == "sair" :
        print("Codigo finalizado")
        break
    
      
      try :
          entrada_int = int(entrada)

          if entrada_int >= 0 and entrada_int <= 11:
              print("Bom dia")
          elif entrada_int >= 12 and entrada_int <= 17:
              print("Boa Tarde")
          elif entrada_int >= 18 and entrada_int <= 23:
              print("Boa noite")
          else:
              print("Hora não reconhecida pelo programa tente novamente")    

      
      except:
          print(" Por favor digite apenas numeros inteiros ")
          
