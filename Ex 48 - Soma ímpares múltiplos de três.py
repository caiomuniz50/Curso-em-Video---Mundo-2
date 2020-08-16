'''Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3
 e que se encontream no intervalo de 1 ate 500'''

cont = 0
somatorio = 0
for i in range(1, 500):
	if i % 2 == 1 and i % 3 == 0:
		cont = cont + 1
		somatorio = somatorio + i
print('A soma dos %d valores é %d' %(cont, somatorio))