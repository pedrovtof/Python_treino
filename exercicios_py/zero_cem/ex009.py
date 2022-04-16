p = float(input('Insira valor total : '))
d = float(input('Insira valor desconto total[1-100] : '))
desconto = p - ((d/100)*p)
print(f'O Valor de {p} á {d}% é {desconto}')
