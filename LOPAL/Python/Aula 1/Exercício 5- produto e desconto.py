#-*- coding: UTF-8 -*-

print("Diga o valor de uma mercadoria e seu percentual de desconto. Que eu lhe direi o valor de desconto e o total a ser pago")
preço = int(input("Informe o valor da mercadoria: "))
desconto = int(input("Informe o valor de seu percentual de desconto: "))
             
valor = preço * desconto /100
total = preço - valor
             
print("O valor do desconto é de: ", valor, "Já o preço total a ser pago é de: ", total)
            
