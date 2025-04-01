#-*- coding: UTF-8 -*-

soma_pares = 0 
soma_impares = 0

print("Olá usuário, você irá ler vários números inteiros e positivos e no final mostra a soma dos pares e a soma dos ímpares  e parar quando for digitado um número maior que 1000")
 
while True:
    num = int(input("Digite um número positivo ou maior que 1000 para encerrar: "))
    if num > 1000:
        break
    elif num % 2 == 0:
        soma_pares += num
    elif num % 2 != 0:
        soma_impares += num
        
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
