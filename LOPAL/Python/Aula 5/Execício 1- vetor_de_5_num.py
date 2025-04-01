#-*- coding: UTF-8 -*-

grupo = []

print("Olá usuário, digite alguns números e eu lhe mostrarei eles!")

x = 1

for i in range(1, 6):
    valor = int(input(f"Digite o {x}º número:"))
    grupo.append(valor)
    x += 1

print(f"{grupo}")
      
