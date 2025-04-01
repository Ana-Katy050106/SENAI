#-*- coding: UTF-8 -*-

print("Diga por quantas horas você trabalha e eu direi o valor do seu salário líquido")
horas = int(input("Digite por quantas horas você trabalha: "))

total = horas * 19.50

if horas <= 0:
        print("O valor não é válido. Tente de novo.")

elif total > 1500.00:
    result = total * 0.10
    print("O seu salário líquido é de: ", result)

else:
    result = total
    print("O seu salário líquido é de: ", result)
            
