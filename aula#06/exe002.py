# Maior de idade

nome = input('Nome->')
idade = input('Idade->')

idade = int(idade)

'''
Em portugol
se idade for > que  18 ou idade for = 18 faça:
    escreva('MAIOR DE IDADE!')
'''

if idade > 18 or idade == 18:
    print(f'Olá, {nome}! você tem {idade} anos. LOgo você é maior de idade.')

if idade < 18:
    print(f'Olá, {nome}! você tem {idade} anos. LOgo você é menor de idade.')
