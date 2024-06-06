lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # n posso jogar isso em uma variavel e depois usar , pois o extende esta mexendo diretamente com a variavel inicial a
print(lista_a)