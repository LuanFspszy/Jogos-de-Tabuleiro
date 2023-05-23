import os
from time import sleep
os.system('cls' or None)
def monttab(tab):
    os.system('cls' or None)
    print('='*5, 'JOGO DA VELHA', '='*5)
    for i, c in enumerate(tab):
        for l in c:
            print(f'{l:3}', end='')
        print()



tabuleiro = [['', '1', '2', '3'], ['1', '-', '-', '-'], ['2', '-', '-', '-'], ['3', '-', '-', '-']]

vez = 'X'
cordenadas = [0, 0]
cont = 0
vezo = vezx = 0
vencedor = ''

while True:
    cont += 1
    if vez == 'X':
        #montadndo tabuleiro
        vezx += 1
        monttab(tabuleiro)
        print(f'é a {vezx}° vez do X')

        #lendo cordenadas
        while True:
            while True:
                intr = input('digite a coluna: ')

                if intr not in ['1', '2', '3']:
                    print('valor invalido, digite valores entre 1 e 3')
                else:
                    cordenadas[0] = int(intr)
                    break

            
            while True:
                intr = input('digite a fileira: ')

                if intr not in ['1', '2', '3']:
                    print('valor invalido, digite valores entre 1 e 3')
                else:
                    cordenadas[1] = int(intr)
                    break
            
            if tabuleiro[cordenadas[1]][cordenadas[0]] != '-':
                print('posição ocupada!')
            else:
                tabuleiro[cordenadas[1]][cordenadas[0]] = 'X'
                break
        vez = 'O'


    elif vez == 'O':
        vezo += 1
        monttab(tabuleiro)
        print(f'é a {vezo}° vez do O')

        #lendo cordenadas
        while True:
            while True:
                intr = input('digite a coluna: ')

                if intr not in ['1', '2', '3']:
                    print('valor invalido, digite valores entre 1 e 3')
                else:
                    cordenadas[0] = int(intr)
                    break

            
            while True:
                intr = input('digite a fileira: ')

                if intr not in ['1', '2', '3']:
                    print('valor invalido, digite valores entre 1 e 3')
                else:
                    cordenadas[1] = int(intr)
                    break
            
            if tabuleiro[cordenadas[1]][cordenadas[0]] != '-':
                print('posição ocupada!')
            else:
                tabuleiro[cordenadas[1]][cordenadas[0]] = 'O'
                break
        vez = 'X'

    #verificando vitória

    for z in tabuleiro:
        if z[1] == z[2] and z[2] == z[3] and z[1] != '-':
            vencedor = z[1]

    cont = 1
    while cont < 4:
        if tabuleiro[cont][1] == tabuleiro[cont][2] and tabuleiro[cont][2] == tabuleiro[cont][3] and tabuleiro[cont][1] != '-':
            vencedor = tabuleiro[cont][1]
        cont += 1

    c = l = 1
    while True:
        if tabuleiro[l][c] == tabuleiro[l+1][c] and tabuleiro[l+1][c] == tabuleiro[l+2][c] and tabuleiro[l][c] != '-':
            vencedor = tabuleiro[l][c]
            break
        c += 1
        if c == 3:
            break

    if tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[2][2] == tabuleiro[3][3] and tabuleiro[1][1] != '-':
        vencedor = tabuleiro[1][1]

    if tabuleiro[1][3] == tabuleiro[2][2] and tabuleiro[2][2] == tabuleiro[3][1] and tabuleiro[1][3] != '-':
        vencedor = tabuleiro[1][3] 

    if vezx + vezo == 9 and vencedor == '':
        vencedor = 'velha'
        break

    if vencedor != '':
        break

monttab(tabuleiro)

print(f'o vencedor foi: {vencedor}')