v1 = input('Digite o 1º valor: ')
v2 = input('Digite o 2º valor: ')
v3 = input('Digite o 3º valor: ')

if v1 < v2 and v1 < v3:
    print( v1 )
else: 
    if v3 < v2 and v3 < v1:
        print(v3)
    else:
        print(v2)
