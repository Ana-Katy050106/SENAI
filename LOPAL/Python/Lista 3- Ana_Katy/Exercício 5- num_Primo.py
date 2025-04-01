#-*- coding: UTF-8 -*-

print("Digite um número e eu lhe direi se ele é primo ou não")

def verificar_primo(numero):
    if numero <= 1:
        return f"O número {numero} não é primo!"
   
    for i in range(2, numero):
        if numero % i == 0:
            return f"O número {numero} não é primo!"
   
    return f"O número {numero} é primo!"

numero = int(input("Digite um número para verificar se é primo: "))

resultado = verificar_primo(numero)
print(resultado)
