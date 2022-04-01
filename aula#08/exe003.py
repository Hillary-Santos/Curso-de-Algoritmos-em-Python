l1 = input('Digite o 1º lado do triângulo: ')
l2 = input('Digite o 2º lado do triângulo: ')
l3 = input('Digite o 3º lado do triângulo: ')

if  l1 == l2 and l1 == l3 and l3 == l1:
    print('Esse é um triângulo ESCALENO!')
else:
    # l1 == l2 ou l1 == l3 ou l2 == 3
    if (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and  l2 != l1):
        print('Esse é um triângulo ISÓSCELES!')
    else:
        print("Este é um triângulo EQUILÁTERO!")
