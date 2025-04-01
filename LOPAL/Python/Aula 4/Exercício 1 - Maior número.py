#-*- coding: UTF-8 -*-

print("Olá usuário,você irá escrever um número e eu e direi o maior!")
def maior_num():
    if num1 > num2:
        return num1
    else:
        return num2

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite  segundo número: "))

maior = maior_num()
print(f"O maior número é: {maior}")
