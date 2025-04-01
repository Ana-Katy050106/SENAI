#-*- coding: UTF-8 -*-

print("Informe um número e, dependendo do número, direi a raiz quadrada ou o quadrado do número")
 
import math

num = int(input("Digite seu número: "))

if num >= 0:
     result = math.sqrt(num)
     print("O resultado é: ", result)

else:
    result = num ** 2
    print("O resultado é: ", result)
