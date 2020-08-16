'''Faça um programa que leia um número inteiro e diga se ele é primo'''

num = int(input("Digite um número: "))

contador = 0

for i in range(1, num + 1):
	if num % i == 0:
		contador += 1
if contador == 2:
	print("O número %d é primo!"%(num))
else:
	print("O número %d não é primo!"%(num))