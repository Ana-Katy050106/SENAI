#-*-coding: UTF-8 -*-

print("Oi usuário. Você irá calcular o valor de um aumento de salário")
salário = float(input("Digite o valor do salário: "))
porcent = int(input("Digite a porcentagem do aumento: "))
valor = salário * porcent /100
total = salário + valor
print("O valor do aumento é de: " ,valor,"O seu total é de: ", total)
