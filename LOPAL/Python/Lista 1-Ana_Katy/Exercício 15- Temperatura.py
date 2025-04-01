#-*- coding: UTF-8 -*-

print("Olá usuário, me diga a temperatura e eu te direi como está o clima")

temperatura = int(input("Digite a temperatura: "))

if temperatura <= 0:
    print("Erro! Volte ao início!")
elif temperatura <= 15:
    print("Está muito frio!")

elif temperatura >= 16 and temperatura < 23:
    print("Está frio!")

elif temperatura >= 23 and temperatura < 26:
     print("Está agradável!")

elif temperatura >= 26 and temperatura < 30:
     print("Está calor!")

elif temperatura >= 31:
     print("Está muito quente!")
  
else:
    print("Erro! Volte ao início!")
