'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em
graus Fahrenheit.'''
import math

c = float(input("Insira aqui quantos graus Celsius esta fazendo:"))
f = (c * (9/5)) + 32
print("O valor transformado em Fahrenheit é:" ,f)

'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em 
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1litro
para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que 
custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário as 
quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente
 10% de folga e sempre arredonde os valores para cima, isto é, considere latas 
 cheias.'''

area = int(input("Quantos metros quadrados tem o local?"))
folga = (area * 1.1)
litros_metros = 6
litros_sendo_usados = folga / litros_metros
litro_lata = 18
latas = math.ceil(litros_sendo_usados / litro_lata)
valor_apenas_lata = latas * 80
litro_galao = 3.6
galao = math.ceil(litros_sendo_usados / litro_galao)
valor_apenas_galao = galao * 25

print("Você deverá usar {} latas, no valor de {} reais".format(latas, valor_apenas_lata))
print("ou {} galões, no valor de {} reais".format(galao, valor_apenas_galao))

numero_latas = math.floor(litros_sendo_usados / litro_lata)
valor_lata = latas * 80
litros_falta = litros_sendo_usados % litro_lata
numero_galao = math.ceil(litros_falta / litro_galao)
valor_galao = numero_galao * 25

valor_total = valor_lata + valor_galao

print("Você deverá usar {} latas de 18 litros mais {} galões de 3.6 litros, totalizando "
      "{} reais".format(numero_latas,numero_galao, valor_total))

'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar 
M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" 
ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = str(input("Olá, por favor informe em qual turno você estuda, sendo M para"
                     " matutino, V vespertino e N noturno:"))
if (turno=="M"):
    print("Você estuda pela manhã, então, bom dia!")
elif (turno=="V"):
    print("Você estuda a tarde, então, boa tarde!")
elif (turno=="N"):
    print("Você estuda a noite, então, boa noite!")
else:
    print("Valor inválido")

'''Faça um programa que leia e valide as seguintes informações:Nome: maior que 3 
caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

nome = input("Informe seu nome:")
print("Seu nome é:" ,nome)
idade = int(input("Informe sua idade:"))
if idade >= 151:
        print("Valor invalido")
else:
    print("Você tem {} anos".format(idade))
salário = float(input("Informe seu salário: R$"))
if salário == 0:
    print("Esta desempregadx!")
else:
    print("Recebe R$" ,salário)
sexo = input("Informe seu sexo sendo F para feminino e M para masculino:")
if (sexo == "F"):
    print("Seu sexo é feminino")
elif (sexo == "M"):
    print("Seu sexo é masculino")
estado_civil = input("Informe seu estado civil sendo S para solteirx, C casadx,"
                     " V viuvx e D divorciadx:")
if (estado_civil == "S", sexo == "F"):
    print("Seu estado civil é solteira")
elif(estado_civil == "S", sexo == "M"):
    print("Seu estado civil é solteiro")
elif (estado_civil == "C", sexo == "F"):
    print("Seu estado civil é casada")
elif(estado_civil == "C", sexo == "M"):
    print("Seu estado civil é casado")
elif(estado_civil == "V", sexo == "F"):
    print("Seu estado civil é viuva")
elif(estado_civil == "V", sexo == "M"):
    print("Seu estado civil é viuvo")
elif(estado_civil == "D", sexo == "F"):
    print("Seu estado civil é divorciada")
elif(estado_civil == "D", sexo == "M"):
    print("Seu estado civil é divorciado")

'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''
primeiro_bi = float(input("Informe sua nota do primerio bimestre:"))
segundo_bi = float(input("Informe sua nota do segundo bimestre:"))
terceiro_bi = float(input("Informe sua nota do terceiro bimestre:"))
quarto_bi = float(input("Informe sua nota do quarto bimestre:"))

media = (primeiro_bi + segundo_bi + terceiro_bi + quarto_bi)/4

print("Sua média do ano foi de: " ,media)