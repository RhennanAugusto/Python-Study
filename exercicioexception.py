numero = input("Esse numero digitado vai ser dobrado:")


try:
    numero_float = float(numero) # utilizo essa forma para corrigir o erro de estar sendo uma string 
    print('FLOAT:', numero_float)
    print(f"O dobro do {numero} é {numero_float*(2)}")

except:
    print("Isso não é um numero") # NÃO é muito comum usar esse try dessa forma , mas nesses exercicios podemos continuar dessa forma