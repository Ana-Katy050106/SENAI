#-*- coding: UTF-8 -*-

print("""Numa faculdade, os alunos com média maior ou igual a 7,0 são aprovados, aqueles
com média inferior a 3,0 são reprovados e os demais ficam de recuperação. De acordo com as notas do aluno informe sua situação""")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
if media >= 7:
    print("Você foi aprovado por nota.Parabéns!")
    
elif media <= 3:
    print("você foi reprovado")
    
else:
    print("Você está de recuperação")
