#-*- coding: UTF-8 -*-

print("Olá usuário, você irá ler três notas e o número de faltas de um aluno e escrever qual a sua situação final")
N1 = float(input("Digite qual foi a sua primeira nota: "))
N2 = float(input("Digite qual foi a sua segunda nota: "))
N3 = float(input("Digite qual foi a sua terceira nota: "))
Faltas = int(input("Digite qual foi a sua quantidade de faltas: "))

media = (N1 + N2 + N3) / 3
LimdeFaltas = 80 * 0.25

if media > 7 and Faltas < LimdeFaltas:
    print("Você foi aprovado.")
elif media < 7 and Faltas > LimdeFaltas:
    print("Você foi reprovado por falta e por média.")
elif Faltas >= LimdeFaltas:
    print("Você foi reprovado por falta.")
elif media < 7:
    print("Você foi reprovado por média.")
else:
    print("Erro.")
