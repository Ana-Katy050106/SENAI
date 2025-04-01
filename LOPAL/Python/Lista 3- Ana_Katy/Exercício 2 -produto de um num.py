#-*- coding: UTF-8 -*-

print("Digite um número e eu lhe direi a mutiplicação dele.")

numero = int(input("Digite um número inteiro positivo: "))
produto = 1
digito = 0
while numero > 0:
        digito = numero%10
        numero//=10
        produto *= digito 
print (produto)
