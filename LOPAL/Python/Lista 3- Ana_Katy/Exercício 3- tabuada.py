#-*- coding: UTF-8 -*-

print("Oi usuário, digite um número e eu lhe direi a tabuada dele")

def tabela_multiplicacao(numero):
    for i in range(1, 11):  
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Digite um número para gerar a tabela de multiplicação: "))

tabela_multiplicacao(numero)
