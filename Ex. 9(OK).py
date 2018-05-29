# Faça um Programa que leia três números e mostre-os em ordem decrescente.

print('Inicio do programa.')
print()


valid_n = False

while valid_n == False:
    n1 = (input('Primeiro numero: '))
    try:
        n1 = int(n1)
        valid_n = True
    except:
        print('Erro, digite somente numeros.')

valid_n = False
while valid_n == False:
    n2 = (input('Segundo numero : '))
    try:
        n2 = int(n2)
        valid_n = True
    except:
        print('Erro, digite somente numeros.')

valid_n = False
while valid_n == False:
    n3 = (input('Terceiro numero: '))
    try:
        n3 = int(n3)
        valid_n = True
    except:
        print('Erro, digite somente numeros.')

valid_n = False

print(n1, '-', n2, '-', n3)

if n3 > n2:
    v = n3
    n3 = n2
    n2 = v

if n2 > n1:
    v = n2
    n2 = n1
    n1 = v

if n3 > n2:
    v = n3
    n3 = n2
    n2 = v

print(n1, '-', n2, '-', n3)

print()
input('Aperte enter para sair')