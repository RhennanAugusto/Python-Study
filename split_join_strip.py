frase = " Olha só que , coisa interessante "
lista_palavras_cruas = frase.split(',')

lista_palavras = []
for i, frase in enumerate(lista_palavras_cruas):
    lista_palavras.append(lista_palavras_cruas[i].strip()) #tira os espaços da frase

print(lista_palavras_cruas)
print(lista_palavras)


frases_unidas = '-'.join(lista_palavras) # metódo de como fazer a junção de string com base no que foi passado entre aspas
print(frases_unidas)