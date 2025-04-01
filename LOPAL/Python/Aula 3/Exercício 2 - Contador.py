#-*- coding: UTF-8 -*-

print("Olá usuário, você irá digitar números positivos e eu lhe direi quantos números foram digitados.")

contador = 0

while True:
    num = int(input("Digite um número: "))
    if num < 0:
        print("Você escolheu sair. Até logo!")
        break
    contador = contador + 1
    
print(f"A quantidade de números digitados foi de {contador} números.")
        

    
    
    
