x = float(input('Quantos KM o carro rodou? '))
y = float(input('Quantos dias durou o aluguel? '))
z = (60*y)+(x*0.15)
print('O valor total a pagar pelo aluguel é R${:.2f}'.format(z))