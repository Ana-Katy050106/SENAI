#-*- coding: UTF-8 -*-

print("Olá usuário, você irá ler dois números e informar se o primeiro é divisível pelo segundo")

A= int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
        

if B == 0:
        print("Não é divisível por: ", B,)

elif A % B == 0:
    print("É divisível por: ", B,)

else:
    print("Não é divisível por: ", B)
