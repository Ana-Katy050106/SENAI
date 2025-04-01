#-*- coding: UTF-8 -*-

print("Digite seu peso e a sua altura, e eu lhe direi se você está com um peso favorável ou não.")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso / (altura ** 2)

if IMC < 0:
        print("a altura e o peso são inválidos.")
elif IMC < 20:
    print("Você está abaixo do peso.")

elif IMC >= 20 and IMC < 25:
    print("Você está com o peso normal.")

elif IMC >= 25 and IMC < 30:
    print("Você está acima do peso.")

elif IMC >= 30 and IMC < 40:
    print("Você está obeso.")

else:
    print("Você é peso mórbito.")
    
