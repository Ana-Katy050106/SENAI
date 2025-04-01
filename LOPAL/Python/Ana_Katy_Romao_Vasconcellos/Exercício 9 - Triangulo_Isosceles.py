#-*- coding: UTF-8 -*-


print("Olá usuário, digite o comprimento dos três lados de um triângulo e eu lhe direi se ele é isóscel5es ou não.")

a = int(input ("Me informe o primero número: "))
b = int(input ("Me informe o segundo número: "))
c = int(input ("Me informe o terceiro número: "))

valor = a + b
valor2 = b + c
valor3 = c + a

if valor < c or valor2 < a or valor3 < b:
    print("Ocorreu um erro, faça novamente!")

elif a == b and a != c or a == c and a != b or b == c and b != a:
    print("Seu triângulo é isósceles.")
    
else:
    print("Seu triângulo não é isósceles.")
