#-*- coding: UTF-8 -*-

print("Olá usuário, Digite a quantidade de dias de atraso e eu lhe direi o valor da multa.")

quant_dias = int(input("Digite a quandidade de dias de atraso: "))

if  quant_dias <= 10:
    dia = quant_dias * 2

elif quant_dias > 10:
    dia = quant_dias  * 3

print(f"o valor da multa é de: {dia}R$ a mais")

