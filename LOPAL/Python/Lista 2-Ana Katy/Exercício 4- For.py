#-*- coding: UTF-8 -*-

n = int(input("Digite um número para encontrar seus divisores: ")) 

print(f"Divisores de {n}:")

for i in range(1, n + 1): 
 if n % i == 0:
     print(i)
