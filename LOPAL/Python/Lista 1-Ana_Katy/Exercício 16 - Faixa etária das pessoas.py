#-*- coding: UTF-8 -*-

print("Oi usuário, você irá classificar a faixa etária das pessoas conforme a idade que for informada para")

idade = int(input("Digite a sua idade: "))

if idade <= 0:
    print("Erro! Volte ao início!")
elif idade < 2:
    print("Você é um bebê!")

elif idade > 2 and idade < 12:
    print("Você é uma criança!")

elif idade > 12 and idade < 23:
    print("Você é um adolescente!")

elif idade > 23 and idade < 70:
    print("Você é um adulto!")

elif idade > 70:
    print("Você é um idoso!")
    
else:
    print("Erro! Volte ao início!")
