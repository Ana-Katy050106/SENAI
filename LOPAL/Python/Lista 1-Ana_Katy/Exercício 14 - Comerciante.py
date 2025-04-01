#-*- coding: UTF-8 -*-

print("Olá usuário, me dê o valor do seu produto que eu te darei o valor total dele com um lucro de 45% CASO o valor da compra for menor que R$20,00!")

num = float(input ("Me diga o valor do produto: "))

if num <=20:
    conta = (num * 45 / 100) + num
    print("O valor que ele deve ser vendido é de: ", conta)
if num >=20:
    conta = (num * 30 / 100) + num
    print("O valor no qual ele deve ser vendido é de: ", conta)


