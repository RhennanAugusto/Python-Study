while True:
   nome_usuario = input("Digite seu primeiro nome aqui: ")
   if nome_usuario.lower() == "sair":
      print("Código finalizado")
      break
   
   
   try:
       if nome_usuario.isalpha(): # Aqui eu utilizo o is.alpha para verificar se na variavel nome_usuario só contem letras se sim o bloco segue , caso contrario entramos no else 
         #usando o .isalpha tiramos da frente qualquer empecilho caso a pessoa não digite 
         #ou a pessoa digite apenas espaços e num junto com as letras :)
         tamanho = len(nome_usuario)
        
         if tamanho <= 4 :
            print("Seu nome é curto ")
         elif tamanho>= 5 and tamanho <=6 :
            print("Seu nome é de tamanho regular")
         else:
            print("Seu nome é grande")
       else:
         raise ValueError("Você não digitou um nome valido , tente novamente")# crio esse tipo de exceção personalizada e essa mensagem vai ser exibida quando a execeção for capturada , quando esse raise é lançado o python começa a procurar um bloco except para lidar com essa exceção e no nosso codigo existe esse bloco 

   except ValueError as e: #o 'as e' é onde eu estou associando a exceção capturada a uma variavel  chamada 'e' isso permite que eu acesse informações sobre a exceção 
      print("Tipo da exceção:", type(e)) # eu associei a exceção a variavel definida como e
      print("Mensagem de erro:", e)
      
      