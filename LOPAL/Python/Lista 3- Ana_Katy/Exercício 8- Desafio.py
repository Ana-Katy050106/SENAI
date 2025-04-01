#-*- coding: UTF-8 -*-

print("Digite um número e eu lhe direi quantos dígitos ele tem.")

def contar_digitos(numero):
    count = 0
    while numero > 0:
        numero //= 10  
        count += 1  
    return count


numero = int(input("Digite um número: "))

resultado = contar_digitos(numero)

print(f"O número {numero} tem {resultado} dígitos.")
