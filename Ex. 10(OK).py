# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('Inicio do Programa.')
print()

lista_de_variavel = ['m', 'v', 'n']

valid_input = False

while valid_input == False:
    turno = input('Digite o turno que você estuda. M-matutino ou V-Vespertino ou N- Noturno: ').lower()
    if turno in lista_de_variavel:
        valid_input = True
    else:
        print('Erro, Digite somente uma das opções informadas.')

if turno == 'm':
    print('Bom dia')
elif turno == 'v':
    print('Boa Tarde')
elif turno == 'n':
    print('Boa Noite')
else:
    print('Erro, Contate o administrador.')

print()
input('Aperte enter para sair')