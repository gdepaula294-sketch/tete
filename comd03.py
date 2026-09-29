#3. Desafio do resto: escreva uma expressão usando % que descubra se um número é par ou ímpar (dica: numero % 2).
n1 = int(input('Digite seu número: '))

#Calculo de par ou impar 
par = n1 % 2
if par == 0:
    print('O seu número é par')
else:
    print('O seu númeor é impar')
