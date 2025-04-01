# -*- coding: UTF-8 -*-


print("Olá usuário! Digite algo que eu lhe direi quantas concoantes foram lidas.")

cont = 0
contadorconsoantes = 0
lista = []

cons = input("Digite uma palavra com até 10 letras: ")

for i in range(len(cons)):
    if cons[i] == "a" or cons[i] == "e"  or cons[i] == "i"  or cons[i] == "o"  or cons[i] == "u":
        cont = 0
    else:
        contadorconsoantes += 1

print(f"Você digitou: {contadorconsoantes} consoantes")

    








