#-*- coding: UTF-8 -*-

cont21 = 0
cont50 = 0

print("Olá usuário, digite o total de pessoas com menos de 21 anos e o total de pessoas com mais de 50 anos.")

while True:
    idade = int(input("Digite uma idade: "))
    if idade == -99:
        print(f"A quantidade de pessoas menor que 21 é {cont21} e maior que 50 é {cont50}")
        break
    elif idade < 21:
        cont21 += 1
    elif idade > 50:
        cont50 += 1
    

