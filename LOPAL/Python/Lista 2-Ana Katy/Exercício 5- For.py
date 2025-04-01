#-*-  coding: UTF-8 -*-

tabuada = 1

for tabuada in range (0, 10):
    num = 0
    print(f"""---------------
Tabuada do {tabuada}
          """ )
    for num in range (0,11):
        print(f"{tabuada} X {num} = {tabuada * num}")

print("---------------")
