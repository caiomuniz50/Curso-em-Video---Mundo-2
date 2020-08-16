'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo
desconsiderando os espaços'''

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')

if frase == frase[::-1]:
	print('palindromo')
else: 
	print('não é palindromo')


