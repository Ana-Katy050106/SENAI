#-*- coding: UTF-8 -*-

print("Me diga o seu salário bruto e o valor da prestação, que eu ire informar se o empréstimo pode ou não ser concedido.")

salario = float(input("Digite o valor do seu salário: "))
prestacao = float(input("Digite o valor da prestação : "))

if prestacao > salario * 0.30:
    print("O empréstimo não é válido")

else:
    print("O empréstimo é válido. Uhuul!")


