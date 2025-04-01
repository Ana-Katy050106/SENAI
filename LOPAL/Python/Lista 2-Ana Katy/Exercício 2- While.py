#-*- coding: UTF-8 -*-

maior = 0
menor = 0

print("Olá usuário, você irá digitar alguns números e eu lhe direi qual é o maior e qual é o menor!")

while True: 
 
 num = int(input("Digite um número e digite negativo para encerrar: "))
 
 if num < 0:
     print("Você escolheu sair. Tchau :D!")
     print(f"O maior número é {maior}.")
     print(f"O menor número é {menor}.") 
     break
 
 elif maior == 0 or num > maior:
     maior = num
     
 elif menor == 0 or num < menor:
     menor = num

 elif maior != 0 and menor != 0:
    print(f"O maior número é {maior}.")
    print(f"O menor número é {menor}.") 

else:
    print("Nenhum número válido foi inserido.")
