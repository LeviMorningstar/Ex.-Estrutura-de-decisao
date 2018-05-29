#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

print('Inicio do Programa.')
print()

valid_n1 = False
valid_n2 = False

while valid_n1 == False:
    n1 = input('Digite o valor da primeira prova: ')
    print()
    try:
        n1 = float(n1)
        if n1 >10:
            print('Erro, o valor nao pode ultrapassar 10')
        else:
            valid_n1 = True
    except:
        print()
        print('Erro, digite um valor valido.')
        print()

while valid_n2 == False:
    n2 = input('Digite o valor da Segunda nota:')
    print()
    try:
        n2 = float(n2)
        if n2 >10:
            print('Erro, o valor nao pode ultrapassar 10')
        else:
            valid_n2 = True
    except:
        print('Erro, digite um valor valido.')

media = (n1+n2) / 2

if media == 10:
    print('Aprovado com Distinção.')
elif media >= 7:
    print('Aprovado.')
else:
    print('Reprovado.')

print()
print('Fim do programa')
print()
input('Aperte enter para sair.')