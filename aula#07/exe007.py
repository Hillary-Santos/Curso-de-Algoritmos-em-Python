p1 = input('Digite a 1º nota: ')
p2 = input('Digite a 2º nota: ')
p3 = input('Digite a 3º nota: ')

p1 = float(p1)
p2 = float(p2)
p3 = float(p3)

# ordem de precedência

media = (p1 + p2 + p3) / 3

if media >= 7 :
    print('Parabéns, você PASSOU de ano!')
else:
    print('você REPROVOU!')    