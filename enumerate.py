lista = ['Maria','Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

for item in lista_enumerada: #posso usar o for para trazer os indices e os nomes, mas dessa forma eun consigo usar mais for no codigo
    print(item)


#### para mudar esse problema uso direto o enumerate que é como se ele criasse um iterator sempre e assim posso usar quantos forms puder
for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)
for item in enumerate(lista):
    print(item)
###
for indice,nome in enumerate(lista): #aqui posso acessar os valores direto fora da tupla
    print(indice,nome)