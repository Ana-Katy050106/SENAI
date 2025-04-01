#-*- coding: UTF-8 -*-

print("Olá usuário,  me diga a altura e o raio do cilindo e eu lhe direi o volume!")

def calcular_volume_cilindro(raio, altura):
    volume = 3.14  * (raio ** 2) * altura
    return volume

raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

volume = calcular_volume_cilindro(raio, altura)
print(f"O volume do cilindro é: {volume:.2f}")


