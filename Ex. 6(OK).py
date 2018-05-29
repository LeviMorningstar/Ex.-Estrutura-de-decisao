# Faça um Programa que leia três números e mostre o maior deles.

print('Inicio do Programa')
print()

valid_numero = False

while valid_numero == False:
    print()
    n1 = input('Digite o Primeiro número: ')
    print()
    try:
        n1 = int(n1)
        valid_numero = True
    except:
        print('==='*15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('==='*15)

valid_numero = False

while valid_numero == False:
    print()
    n2 = (input('Digite o segundo número:'))
    print()
    try:
        n2 = int(n2)
        valid_numero = True
    except:
        print('===' * 15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('===' * 15)

valid_numero = False

while valid_numero == False:
    print()
    n3 = (input('Digite o terceiro número:'))
    print()
    try:
        n3 = int(n3)
        valid_numero = True
    except:
        print('===' * 15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('===' * 15)

valid_numero = False

if n1 > n2 and n3:
    print('O maior numero é:', n1)
else:
    if n2 > n3:
        print('O maior numero é:', n2)
    if n3 > n2:
        print('O maior numero é:', n3)
    else:
        print('Erro')

print()
input('Aperte enter para sair')