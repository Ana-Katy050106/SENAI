#-*- coding: UTF-8 -*-

print("Olá usuário, me diga a sua idade e eu lhe direi a sua classe eleitoral")

def classe_eleitoral():
    idade = print(input("Digite a sua idade: "))
    if idade < 16:
        return "Não-eleitor"
    elif idade > 18 and idade < 65:
        return "Eleitor obrigatório"
    elif idade >= 16 and idade <= 18 or idade >= 65:
        return "Eleitor facultativo"

print(classe_eleitoral())
