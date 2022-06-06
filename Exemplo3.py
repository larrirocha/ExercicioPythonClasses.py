'''Fazer um programa que solicita o valor de um produto e em seguida solicita o valor
do aumento e como resultado calcular o valor do aumento'''

prod = float(input("Informe o valor do produto:"))
porcent = float(input("Informe quantos porcentos de aumento: "))
valor = (prod + (prod * porcent / 100))

print("O novo valor é: " ,valor)