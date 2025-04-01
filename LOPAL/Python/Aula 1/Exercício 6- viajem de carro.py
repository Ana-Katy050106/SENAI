# -*- coding: UTF-8 -*-

print("Oi usuário. Você irá calcular o tempo de viagem de um carro")
distância = float(input("Qual a distância percorrida em km: "))
velocidade = float(input("Qual a velocidade média para a viagem em km por hora: "))
tempo = distância / velocidade
print("A velocidade média é: ", tempo, "horas")
