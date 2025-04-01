#-*- coding: UTF-8 -*-

print("Diga o a quantidade de itens comprados e o preço. Que eu lhe direi o valor de desconto e o total a ser pago")
itens = int(input("Informe a quantidade de itens: "))
preco = float(input("Informe o preço dos itens: "))

descont1 = (preco * 5)/ 100
descont2 = (preco * 10)/100
total1 = preco - descont1
total2 = preco - descont2

if preco > 10:
    print(f"O seu desconto é de {descont1}")
    print(f"O valor total da compra com o desconto aplicado: {total1}.")

if preco > 20:
    print(f"O seu desconto é de {descont2}")
    print(f"O valor total da compra com o desconto aplicado: {total2}.")
else:
    print("Erro!")


            
