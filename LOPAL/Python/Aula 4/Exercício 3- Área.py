#-*- coding: UTF-8 -*-

print("Olá usuário, me diga o lado do quadrado e eu lhe direi a sua área")

def area():
    area = lado ** 2
    print(area)

lado = int(input("Digite um valor: "))
area()
