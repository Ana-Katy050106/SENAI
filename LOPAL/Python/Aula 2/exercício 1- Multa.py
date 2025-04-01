#-*- coding: UTF-8-*-

pergunta = int(input("Qual a velocidade do seu carro?: "))
             
if  pergunta > 80:
    vm = (pergunta - 80) * 5
    kmacima = pergunta - 80

    print("Você foi multado, pois ultrapassou a velocidade permitida 80 e deverá pagar", (vm) )

elif pergunta < 80:
    print("Você está em uma velocidade de:",pergunta, "o que é permitido! Parabéns!")

else:
    print("Erro!")


             







    
