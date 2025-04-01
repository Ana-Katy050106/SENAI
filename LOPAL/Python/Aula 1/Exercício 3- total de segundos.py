#-*-coding: UTF-8 -*-

print("Oi usuáio. Você lerá a quantidade de dias, horas, minutos e segundos")
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minu = int(input("Digite a quantidade de minutos: "))
segun = int(input("Digite a quantidade de segundos: "))
cond = dias * 86400
conh = horas * 3600
conm = minu * 60
soma = cond + conh +conm + segun
print("O total de segundos é: " ,soma)
