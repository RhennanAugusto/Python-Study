# lista = []
# print(bool(lista))
# lista = [123, True, 'Rhennan', 1.2, []] # separados por indices, cada item desse
# lista[2] = 'Console' # modificando o valor dentro da lista e como o python le da esquerda para direita..
# print(lista[2]) 
lista = [10,20,30,40,50]
numero = lista[4] # definindo variaveis para certos elementos
del lista[2] # deletando um elemento da lista
print(lista)
print(lista[3])
lista.append(60)
lista.pop() # remove o ultimo elemento da lista ou o indice escolhido, posso usar como variavel para saber qual item foi retirado
lista.append(70)
del lista [-1] # existem indices invertidos e -1 sempre vai ser o ultimo numero, bem util quando eu não sei qual é 
lista.append(80)
lista.insert(1,3) #2 metodos , 1 para o indice e o 2 para o valor, o valor meio que encaixa onde eu mandei e todos os outros itens pulam uma casa
print(lista)