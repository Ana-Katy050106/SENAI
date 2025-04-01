#-*- coding: UTF-8 -*-

print("Olá usuário, você irá ler dois números e efetuar a adição dele.Se o número for maior que 20 você irá adicionar mais 8, e se ele for menor ou igual a 20 você irá subtrair 5")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma1 = num1 + num2

if soma1 >20:
    result = soma1 + 8
    print("O resultado é: ",result)

elif soma1 <= 20:
     resposta = soma1 - 5
     print("O resultado é: ", resposta)
