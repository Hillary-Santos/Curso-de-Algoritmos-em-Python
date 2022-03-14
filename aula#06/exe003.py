print('==========================================')
print('==== Verificação de Vencimento da CNH ====')
print('==========================================')
print('Digite no seguinte formato dd/mm/aaaa')
d = input('Digite o dia: ')
m = input('Digite o mês: ')
a = input('Digite o anao: ')
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

if d >= '13' and m >= '03' and a >= '2022':
    print('VENCEU!')

if d != '13' and m == '03' and a == '2022':
    print('MES DO VENCIMENTO!')
