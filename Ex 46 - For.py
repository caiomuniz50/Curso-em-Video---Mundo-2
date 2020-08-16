'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artificio indo de 10 a 0 com pausa de 1 segundo entre eles '''

import time
print('Contagem regressiva:')
for i in range(10, 0, -1):
	time.sleep(1)
	print(i)
print("BOOOM BOOOM POW")
	