#-*- coding: UTF-8-*-

print("Oi usuário, você irá calcular a quantidade de km percorrido por um carro alugado e a quantidade de dias que o carro foi alugado")
km = float(input("Quantidade de km percorrido: "))
dias = int(input("Quantidade de dias que o carro foi alugado: "))

valor1 = dias * 60
valor2 = km * 0.15
total = valor1 + valor2
print("O preço a ser pago é: ", total)
