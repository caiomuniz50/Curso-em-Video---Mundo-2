'''Desenvolva um programa que leia os 6 numeros inteiros e mostre apenas a soma daqueles 
que forem pares. Se o valor digitado for impar, desconsidere-o'''

cont = 0
somatorio = 0
for i in range(1, 7):
	if i % 2 == 0:
		somatorio = somatorio + i
		cont = cont + 1

print("A soma dos %d números pares é %d" %(cont, somatorio))