#-*- coding: UTF-8 -*-

print("Olá usuário, digite um número e eu lhe direi se ele é perfeito ou não!")

numero = int(input("Digite um número inteiro positivo: "))
produto = 1
digito = 0
while numero > 0:
        digito = numero%10
        numero//=10
        produto *= digito 
print (produto)
print("Perfeito" or "Não é perfeito.")
