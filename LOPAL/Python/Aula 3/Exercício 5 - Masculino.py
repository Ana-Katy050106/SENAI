#-*-  coding: UTF-8 -*-

cont = 0

print("Escreva o sexo e eu lhe direi quantas pessoas são de sexo feminino e quantas são de sexo masculino.")
print("Digite M para masculino.")

while True:
    Spessoas = input("Digite:")

    if Spessoas == "m" or Spessoas == "M":
        cont += 1

    elif Spessoas == "sair":
        print(f"Você digitou {cont}")
        break


