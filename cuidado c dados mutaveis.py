lista_a = ['Luiz', 'Maria']
lista_b = lista_a  #desse jeito aqui a lista_b ainda depende e aponta para a lista_a

lista_a[0] = 'Something'
print(lista_b)

####

lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy() #dessa forma eu crio outro lista na memoria e aí é mais facil para um clean code

lista_a[0] = 'Something'
print(lista_b)