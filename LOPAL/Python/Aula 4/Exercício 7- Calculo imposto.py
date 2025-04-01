#-*- coding: UTF-8 -*-

print("Olá usuário, vamos fazer o calculo do imposto")

def soma_Imposto():

    custo= float(input("Digite o valor do custo: "))
    imposto = float(input("Digite o valor do imposto: "))

    taxa_Imposto = (custo * imposto) /100

    total = custo + taxa_Imposto
    return total

print(soma_Imposto())



