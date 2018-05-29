# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

print('Inicio do Programa')
print()

valid_numero = False

while valid_numero == False:
    print()
    n1 = input('Qual o valor da mochila1?')
    print()
    try:
        n1 = float(n1)
        valid_numero = True
    except:
        print('==='*15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('==='*15)

valid_numero = False

while valid_numero == False:
    print()
    n2 = (input('Qual o valor da mochila2?'))
    print()
    try:
        n2 = float(n2)
        valid_numero = True
    except:
        print('===' * 15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('===' * 15)

valid_numero = False

while valid_numero == False:
    print()
    n3 = (input('Qual o valor da mochila3?'))
    print()
    try:
        n3 = float(n3)
        valid_numero = True
    except:
        print('===' * 15)
        print('Erro na entrada de dados, por favor digite somente numeros.')
        print('===' * 15)

valid_numero = False

if n1 < n2 and n1 < n3:
    v = n1
    p = 'mochila1'
elif n2 < n1 and n2 < n3:
    v = n2
    p = 'mochila2'
else:
    v = n3
    p = 'mochila3'
print('Por ser o mais barato, o produto escolhido foi {}, que custa {}R$'.format(p, v))

print()
input('Aperte enter para sair')