#-*- coding: UTF-8 -*-

acum = 0
print("Olá usuário, você irá calcular a soma dos 50 primeiros números pares.")

for i in range(2, 101, 2):
    acum = acum + i
    print(f"{acum}")

if acum <= 0:
    print("Erro!")

print(f"A resposta é igual a {acum}")

    
