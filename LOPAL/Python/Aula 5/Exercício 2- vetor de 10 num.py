#-*- coding: UTF-8 -*-

grupo = []
cont = 1 

print("Olá usuário! Digite alguns números reais e eu lhe direi a ordem inversa deles!")
      
for i in range(1,11):
    valor = float(input(f"{i} - digite o número: "))
    grupo.append(valor)

total = grupo[::-1]

print(f"Os números em ordem inversa são: {total}")
