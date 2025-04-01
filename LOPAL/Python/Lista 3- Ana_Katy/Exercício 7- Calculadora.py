#-*- coding: UTF-8 -*-

print("Digite a operação que eu lhe darei o resultado.")

def adicao(valor1, valor2):
    return valor1 + valor2

def subtracao(valor1, valor2):
    return valor1 - valor2

def multiplicacao(valor1, valor2):
    return valor1 * valor2

def divisao(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return "Erro: Divisão por zero!"

def calculadora():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    operador = input("Digite o operador (+, -, *, /): ")

    if operador == "+":
        resultado = adicao(valor1, valor2)
    elif operador == "-":
        resultado = subtracao(valor1, valor2)
    elif operador == "*":
        resultado = multiplicacao(valor1, valor2)
    elif operador == "/":
        resultado = divisao(valor1, valor2)
    else:
        resultado = "Operador inválido!"

    return resultado

resultado = calculadora()
print(f"Resultado: {resultado}")
