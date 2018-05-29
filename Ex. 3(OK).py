# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print('Inicio do programa.')
print()

print('Esse Programa Informa o Genero informado.')
print()

g = (input('Digite o Genero no Formato "f" para Feminino ou "m" para Masculino: '))
print()

if g == 'f':
    print('Feminino')
elif g == 'm':
    print('Masculino')
else:
     print('Genero Invalido.')

print()
input('Aperte enter para sair')
