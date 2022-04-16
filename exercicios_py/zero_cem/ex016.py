import random
print(' Escolha um nome ')
q = input(' 1: ')
w = input(' 2: ')
e = input(' 3: ')
t = input(' 4: ')
y = q,w,e,t
r = str(random.choice([ q , w , e , t ]))
print(f"O escolhido é o(a) {r}")