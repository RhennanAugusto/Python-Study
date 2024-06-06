qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas :
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1 # por ter esse contador aqui, esse while principal vai ser gerado 5 vezes

    linha += 1 #controlar o corpo do nosso while , como a linha esta fora do 2 while , ela so vai acontecer depois das 5 colunas 

print("Acabou")