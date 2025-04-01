#-*- coding: UTF-8-*-

print("Você irá calcular a redução de vida de um fumante")
cigarros = int(input("Quantos cigarros você fuma por dia: "))
anos = float(input("Quantos anos você fumou: "))

minutosPorCigarros = 10
minutosPorDia = cigarros * minutosPorCigarros
tempoTotalMinu = minutosPorDia * 365 * anos
tempoTotalDias = tempoTotalMinu / (60 * 24)

print("Você perdeu aproximadamente %i dias de vida." %tempoTotalDias)
