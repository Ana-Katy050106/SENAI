#-*- coding: UTF-8 -*-

print("Digite sua nota e eu lhe direi seu conceito.")

def conceito_aluno(nota):
    if nota < 3:
        return "Conceito E"
    elif nota > 3 and nota <= 5:
        return "Conceito D"
    elif nota > 6 and nota <= 7:
        return "Conceito C"
    elif nota > 8 and nota <= 9:
        return "Conceito B"
    elif nota == 10:
        return "Conceito A"
    else:
        return "Nota inválida"


nota = int(input("Digite a nota do aluno: "))

resultado = conceito_aluno(nota)
print(f"A nota {nota} tem o {resultado}.")

