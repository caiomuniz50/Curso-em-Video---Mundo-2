'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher
só que agora utilizando laço for'''

num = int(input("Digite um número que deseja saber a tabudada: "))
for i in range(0, 11):
	mult = num * i
	print(str(num)," * ", str(i), " = ", str( mult))