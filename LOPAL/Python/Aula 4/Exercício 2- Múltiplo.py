#-*- coding: UTF-8 -*-

print("Olá usuário você irá digitar um número e eu te direi se eles são multiplicaveis entre si")

def multiplo():
    if valor1 % valor2 == 0:
        return print("True")
    else:
        return print("False")

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

multiplo()
