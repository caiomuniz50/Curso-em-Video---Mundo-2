'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final
mostre os 10 primeiros termos dessa progressão'''


termo = int(input("Digite o termo da P.A: "))
razao = int(input('Digite a razão da P.A: '))

acumulador = razao

for i in range(0, 10):
	pa = termo + acumulador
	acumulador = acumulador + razao
	print(pa)