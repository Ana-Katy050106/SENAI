#-*- coding: UTF-8 -*-

cont = 0

print("Olá usuário, você irá digitar um número e eu lhe direi quantos números foram digitados")
print("Caso você digite 0, encerrarei o programa!")

while True:
    num = int(input("Digite um número entre 100 e 200: "))

    if num >= 100 and num <= 200:
        cont += 1

    elif num == 0:
        print(f"Ao todo foram utilizados {cont} números entre 100 e 200.")
        break
        
    
    
    
