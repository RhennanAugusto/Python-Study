import decimal #pega uma string e faz a conversão para float para fazer os calculos corretos

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.3f}')
print(round(numero_3, 3)) # função para fazer a chamada em relação a quantidade de número após a vírgula
# mas ele representa o float, ou seja se tudo for zero, depois do número ele não vai mostrar

#usando decimal
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(f"\n{numero_3}")
print(f'{numero_3:.3f}')
print(round(numero_3, 3)) 




