'''Calcule a área de um triangulo

b = float(input("Valor da base é:"))
h = float(input("Valor da altura é:"))
area = (b*h)/2
print("O valor da área é: " , area)

num = [2,5,8,3]
num.append(6)
num.sort()
num.copy()
num.remove(5)
num.pop()
num.append(10)
num.insert(1,6)
if 4 in num:
    num.remove(4)
else:
    print("não existe o numero 4")
print(f"essa lista contem {len(num)} numeros")

valores = []
valores.append(1)
valores.append(2)
valores.append(3)

for c, v in enumerate(valores):
    print(f"na posição {c} encontrei {v}")
print("Cheguei!")'''
