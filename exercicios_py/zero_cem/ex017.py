from random import shuffle
print(' Escolha um nome ')
q = (input(' 1: '))
w = (input(' 2: '))
e = (input(' 3: '))
t = (input(' 4: '))
y = [q, w, e, t]
shuffle(y)
print(f'a ordem dos alunos sera{y}')