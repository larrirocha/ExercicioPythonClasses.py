'''Fazer um programa para informar o número de dias que um respectivo mês possui'''

mes = int(input("Informe o número do mês:"))

if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
    print("O mês informado possui 31 dias")
elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
    print("O mês informado possui 30 dias")
elif (mes == 2):
    print("O mês informado possui 28 dias")
else:
    print("Valor invalido")
