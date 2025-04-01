#-*- coding: UTF-8 -*-

print("Digite a temperatura e o tipo de conversão que eu lhe darei a resposta")

def conversor_temperatura(temperatura, tipo_conversao):
    if tipo_conversao == "Celsius para Fahrenheit":
        return temperatura * 9/5 + 32
    elif tipo_conversao == "Fahrenheit para Celsius":
        return (temperatura - 32) * 5/9
    else:
        return "Tipo de conversão inválido!"


temperatura = float(input("Digite a temperatura: "))
tipo_conversao = input("Digite o tipo de conversão (Celsius para Fahrenheit ou Fahrenheit para Celsius): ")

resultado = conversor_temperatura(temperatura, tipo_conversao)


if tipo_conversao == "Celsius para Fahrenheit":
    print(f"{temperatura}°C = {resultado}°F")
elif tipo_conversao == "Fahrenheit para Celsius":
    print(f"{temperatura}°F = {resultado}°C")
else:
    print(resultado)
