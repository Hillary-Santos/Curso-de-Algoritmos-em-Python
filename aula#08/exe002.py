print('Digite [1] para doar R$ 10,00')
print('Digite [2] para doar R$ 20,00')
print('Digite [3] para doar R$ 30,00')

op = input('Digite uma opção: ')

if op == '1':
    print('Você doou R$ 10,00!')
else:
    if op == '2':
        print('Você doou R$ 20,00!')
    else:
        if op == '3':
            print('Você doou R$ 30,00!')
        else:
            print('Valor inválido!')

