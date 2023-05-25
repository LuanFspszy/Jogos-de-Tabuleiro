from os import system
from time import sleep

def monttab(tab):
    system('cls' or None)
    print('='*5, 'JOGO DA VELHA', '='*5)
    for i, c in enumerate(tab):
        for o, l in enumerate(c):
            if i == 0:
                if o == 3:
                    print(f' {l:^3}', end='', flush=True)
                elif o%2 != 0:
                    print(f'{l:^3} ', end='', flush=True)
                else:
                    print(f'{l:^3}', end='', flush=True)
            elif i == 1 or i == 2:
                if o == 0:
                    print(f'{l:^3}', end='', flush=True)

                elif o == 1 or o == 2:
                    print(f'\033[4m{l:^3}\033[m|', end='', flush=True)
                if o == 3:
                    print(f'\033[4m{l:^3}\033[m', end='', flush=True)

            elif i == 3:
                if o == 0:
                    print(f'{l:^3}', end='', flush=True)

                elif o == 1 or o == 2:
                    print(f'{l:^3}|', end='', flush=True)
                elif o == 3:
                    print(f'{l:^3}', end='', flush=True)
        print()

sair = False
while True:
    while True:
        system('cls' or None)
        print('-='*5, 'MENU', '=-'*5, '\n[1] Jogar\n[2] Regras\n[0] Sair')
        ação_intr = input('O que fazer: ')
        if ação_intr in ['0', '1', '2']:
            ação = int(ação_intr)
            break
        else:
            print('\033[31mValor invalido!\nDigite um valor correspondente a uma das opções\033[m')
            sleep(3)
    
    if ação == 0:
        break

    elif ação == 1:
        while True:
            system('cls' or None)
            print('-'*7, 'JOGOS', '-'*7, '\n[1] Jogo da velha\n[m] Menu\n[0] Sair')
            ação_intr1 = input('O que fazer: ').upper()
            if ação_intr1 in ['0', '1', 'M']:
                ação1 = ação_intr1
                break
            else:
                print('\033[31mValor invalido!\033[m\nDigite um valor correspondente a uma das opções\n')
            sleep(2)
        
        if ação1 == '0':
            sair = True
            break
            

        if ação1 == '1':
            while True:
                system('cls' or None)
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
                                    print('\033[31mValor invalido, digite valores entre 1 e 3\033[m')
                                else:
                                    cordenadas[0] = int(intr)
                                    break

                            
                            while True:
                                intr = input('digite a fileira: ')

                                if intr not in ['1', '2', '3']:
                                    print('\033[31mValor invalido, digite valores entre 1 e 3\033[m')
                                else:
                                    cordenadas[1] = int(intr)
                                    break
                            
                            if tabuleiro[cordenadas[1]][cordenadas[0]] != '-':
                                print('\033[33mPosição ocupada!\033[m')
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
                                    print('\033[31mValor invalido, digite valores entre 1 e 3\033[m')
                                else:
                                    cordenadas[0] = int(intr)
                                    break

                            
                            while True:
                                intr = input('digite a fileira: ')

                                if intr not in ['1', '2', '3']:
                                    print('\033[31mValor invalido, digite valores entre 1 e 3\033[m')
                                else:
                                    cordenadas[1] = int(intr)
                                    break
                            
                            if tabuleiro[cordenadas[1]][cordenadas[0]] != '-':
                                print('\033[33mPosição ocupada!\033[m')
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

                    c = 1
                    while True:
                        if tabuleiro[1][c] == tabuleiro[2][c] and tabuleiro[2][c] == tabuleiro[3][c] and tabuleiro[1][c] != '-':
                            vencedor = tabuleiro[1][c]
                            break
                        c += 1
                        if c == 4:
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
                sleep(3)
                
                while True:
                    jgrnv_intr = input('Deseja jogar novamente?[S/N] ').upper()
                    if jgrnv_intr in ['S', 'N']:
                        jgrnv = jgrnv_intr
                        break
                    else:
                        print('\033[31mValor invalido\033[m\nDigite um valor correspondente a uma opção')

                if jgrnv == 'N':
                    break


    elif ação == 2:
        system('cls' or None)
        print('~~'*3, 'Regras', '~~'*3)
        while True:
            rgrjg_itr = input('[1] Jogo da velha\n[M] Menu\n[0] Sair\nO que fazer: ').upper()
            if rgrjg_itr in ['1', 'M', '0']:
                rgrjg = rgrjg_itr

                if rgrjg == '1':
                    system('cls' or None)
                    print('-----Jogo da velha-----\n\n  -O jogo começa na vez do X\n\n  -Passe as cordenadas iniciando pelas colunas (são as linhas na vertical)\ndepois a fileira (linhas na horizontal)\n\n  -O primeiro que completar uma linha na vertical, horizontal ou diagonal vence\n')
                    sleep(1)
                    input('PRECIONE ENTER PARA VOLTAR PARA O MENU DE REGRAS')
                    system('cls' or None)
                elif rgrjg == 'M':
                    system('cls' or None)
                    break
                elif rgrjg == '0':
                    system('cls' or None)
                    sair = True
                    break
    
    if sair == True:
        break




    