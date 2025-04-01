#-*- coding: UTF-8 -*-

print("Digite um número e eu lhe direi a contagem regressiva")

def contagem_regressiva(numero):
    if numero <= 0:
        print("Erro.")
    else:
        while numero > 0:
            print(numero)
            numero -= 1
        print("Feliz Ano novo!")

numero = int(input("Digite o número para iniciar a contagem regressiva: "))

contagem_regressiva(numero)
