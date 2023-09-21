from random import randint
from time import sleep
import os
import sys

num = ('1','2','3')
itens = ('0', 'Pedra', 'Papel', 'Tesoura')

class color():
    bold = '\033[1m'
    none = '\033[m'
    blue = '\033[0;34m'
    red = '\033[0;31m'
    green = '\033[0;32m'
    cyan = '\033[0;36m'
    yellow = '\033[0;33m'

def limpar():
    os.system('cls')

def menu():
    print(color.green + '◄►' * 15 + color.none)
    print(f'{color.bold + "Bem vindo":^34}')
    print(f'{"JO KEN PÔ":^30}\n {"GAME":^27}')
    print(color.green + '◄►' * 15 + color.none)


limpar()

menu()
sleep(2)
while True:
    resp1 = str(input('Esta pronto para jogar?[sim/não]:')).strip().upper()[0]
    if resp1 in 'SN':
        break
    print(color.red + 'Resposta invalida! Por favor responda somente com "Sim" ou "Não"' + color.none)
if resp1 == 'N':
    print(color.red + 'Finalizando o programa...' + color.none)
    sys.exit()

while True:

    #escolha do bot
    bot_num = randint(1, 4)

    if resp1 == 'S':
        print(color.cyan + 'Escolha uma dessas opções abaixo:' + color.none)
        print(color.yellow + f'{"Pedra[1]":>10}\n{"Papel[2]":>10}\n{"Tesoura[3]":>10}' + color.none)

        #escolha do jogador
        while True:
            player = str(input('sua escolha: ')).strip()
            if player in num:
                break
            print('jogada invalida! Por favor jogue novamente:')
        player = int(player)    

        print('\nJO!')
        sleep(1)
        print('KEN!!')
        sleep(1)
        print('PÔ!!!\n')
        sleep(1.5)

        #tabela de resultados
        print(color.cyan + '≡≡' * 15 + color.none)
        print(f'computador jogou {itens[bot_num]}')
        print(f'jogador jogou {itens[player]}')
        print(color.cyan + '≡≡' * 15 + color.none)

        
        #condições
        if bot_num == 1:
            if player == 1:
                print(color.yellow + 'EMPATE!' + color.none)
            if player == 2:
                print(color.green + 'jogador WIN!' + color.none)
            if player == 3:
                print(color.blue + 'computador WIN!' + color.none)

        if bot_num == 2:
            if player == 2:
                print(color.yellow + 'EMPATE!' + color.none)
            if player == 3:
                print(color.green + 'jogador WIN!' + color.none)
            if player == 1:
                print(color.blue + 'computador WIN!' + color.none)
        
        if bot_num == 3:
            if player == 3:
                print(color.yellow + 'EMPATE!' + color.none)
            if player == 1:
                print(color.green + 'jogador WIN!' + color.none)
            if player == 2:
                print(color.blue + 'computador WIN!' + color.none)
    while True:
        resp2 = str(input('jogar uma nova partida? [sim/não]: ')).strip().upper()[0]
        if resp2 in 'SN':
            limpar()
            break
        print('Resposta invalida! Por favor, responda somente com "Sim" ou "Não" ')
    if resp2 in "N":
        break

print(color.red + 'Finalizando o programa...' + color.none)
sleep(3)
limpar()



