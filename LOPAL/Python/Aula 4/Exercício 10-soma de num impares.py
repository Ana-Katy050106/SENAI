#-*- coding: UTF-8 -*-

print("Digite  alguns números e eu lhe direi a soma dos números ímpares entre eles.")

def soma_impares(A, B):
    soma = 0
    for numero in range(A, B + 1):  
        if numero % 2 != 0:  
            soma += numero
    return soma

A = int(input("Digite o valor de A (menor que B): "))
B = int(input("Digite o valor de B (maior que A): "))

resultado = soma_impares(A, B)
print(f"A soma dos números ímpares entre {A} e {B} é: {resultado}")
