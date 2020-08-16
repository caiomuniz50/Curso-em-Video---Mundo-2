'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
contador = 0
lst = []

for i in range(0, 7):
	idades = int(input('Digite os anos de nascimento: '))
	lst.append(idades)

contador = 0
contador2 = 0

for n in lst:
	if 2020 - n >= 18:
		contador += 1	
	elif 2020 - n < 18:
		contador2 += 1

print("Tivemos %d pessoas maiores que 18 anos"%(contador))
print('E tivemos %d pessoas menores de 18 anos'%(contador2))
