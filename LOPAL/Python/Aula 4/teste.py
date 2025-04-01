#-*- coding: UTF-8 -*-

resultado = 0

def soma():
    global resultado
    num1 = int(input("Valor1: "))
    num2 = int(input("Valor2: "))
    resultado = num1 + num2
    return resultado

soma ()
print("O resultado é", resultado)
