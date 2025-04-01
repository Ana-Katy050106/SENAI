#-*- coding: UTF-8 -*-

print("Olá usuário, irei lhe mostrar todos os números de 1 a 50 e depois essa mesma lista invertida (50 a 1)")

for i in range(1, 51):
 print(i) 
 if i == 50:
     break 

print("""
agora invertido!
""")
 # Reiniciando a contagem de 50 a 1 
for i in range(50, 0, -1): 
 print(i)
 if i == 1:
     break 
