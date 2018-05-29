# Faça um Programa que leia três números e mostre o maior e o menor deles.

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

if n1 < n2 and n1 < n3:
    print('O menor numero é:', n1)

elif n2 < n1 and n2 < n3:
    print('O menor numero é:', n2)
else:
    print('O menor numero é:', n3)


print()
input('Aperte enter para sair')