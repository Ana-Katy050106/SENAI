#-*- coding: UTF-8 -*-

print("Oi usuário, você irá para ler duas variáveis inteiras A e B e garantir que A e B fiquemem ordem crescente")
variavelA = int(input("Digite o primeiro valor: "))
variavelB = int(input("Digite o segundo valor: "))

if variavelA > variavelB:
    A= variavelB
    B= variavelA
    print(f"A ordem crescente é {A} e {B}")

elif variavelA < variavelB:
    A= variavelA
    B = variavelB
    print(f"A ordem crescente é {A} e {B}")

else:
    print("Erro! Volte ao início")
