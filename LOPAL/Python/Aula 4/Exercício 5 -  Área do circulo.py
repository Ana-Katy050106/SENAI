#-*- coding: UTF-8 -*-

print("Olá usuário, diga o raio do circulo e eu lhe direi a área")

def circulo():
    R = float(input("Digite o raio: "))
    return 3.14 * (R ** 2)

area = circulo()
print(area)
