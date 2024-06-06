nome = "Rhennan Augusto"
indice = 0
novo_nome =''

while indice < len(nome):
   letra = nome[indice]
   novo_nome += f'*{letra}'
   indice += 1
   if indice == 15 :
      novo_nome +="*"
print(novo_nome) 
   
   
  