#-*- coding: UTF-8 -*-

nota = []
cont = 1

for i in range(1, 5):
    valor = int(input(f"{cont}. Digite uma nota: "))
    cont += 1
    nota.append(valor)

media = sum(nota) /len(nota)

print(f"A média dos números é equivalente à {media}")
