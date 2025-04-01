#-*- coding: UTF-8-*-

print("Você irá calcular a redução de vida de um fumante")
cigarros = int(input("Quantos cigarros você fuma por dia: "))
anos = float(input("Quantos anos você fumou: "))
qtd_total_cigarros = cigarros * anos * 365
tempo_minutos = qtd_total_cigarros * 10
total_dias = tempo_minutos / 60 / 24 #1440

