#-*- coding: UTF-8 -*-

print("Olá usuário, você irá ler dois números inteiros e escrecer o maior entre eles")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if  num1 > num2:
    print("O primeiro número é o maior número!")

elif num1 < num2:
    print("O segundo número é o maior número!")

else:
    print("Erro!")
