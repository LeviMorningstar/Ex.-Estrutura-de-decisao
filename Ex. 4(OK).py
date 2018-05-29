# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print('Inicio do Programa.')
print()

lista_de_vogais = ['a', 'e', 'i', 'o', 'u']
validando_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]

valid_letra = False

while valid_letra == False:
    letra = input('Digite uma letra: ').lower()
    print()
    if letra not in validando_letras:
        print('Erro na entrada de Dados')
    else:
        valid_letra = True


if letra in lista_de_vogais:
    print('É uma vogal.')
else:
    print('É uma Consoante.')

print()
input('Aperte enter para sair')
