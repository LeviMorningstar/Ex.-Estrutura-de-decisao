# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print('Inicio do Programa')
print()

valid_numero = False
while valid_numero == False:
    print()
    n1 = (input('Digite o número: '))
    print()
    try:
        n1 = int(n1)
        valid_numero = True
    except:
        print('==='*15)
        print('Erro, por favor digite somente numeros.')
        print('===' * 15)


if n1 > 0:
    print('Positivo')
elif n1 == 0:
    print('Numero neutro.')
else:
    print('Negativo')


valid_numero = False
print()
input('Aperte enter para sair')