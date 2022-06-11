from time import sleep
import random
import emoji
lista = ("", emoji.emojize(':punch:', language='alias'), emoji.emojize(':hand:', language='alias'), emoji.emojize(':scissors:', language='alias'))
computador = random.randint(1, 3)
mais = "S"
while mais == "S" or "s":
    computador = random.randint(1, 3)
    jogador = input('''Escolha uma opção:
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA
    ESCOLHA: ''')
    while jogador != '1' and jogador != '2' and jogador != '3':  # se escolher uma opção incorreta
            print('VAI ESCOLHA UMA DAS OPÇÕES AÍ...')
            jogador = input('''Escolha uma opção:
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA
        ESCOLHA: ''')
    jogador = int(jogador)    
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!!!')
    sleep(0.5)
    print('-=' * 10)
    print('EU ESCOLHI: {}'.format(lista[computador]))
    print('VOCÊ: {}'.format(lista[jogador]))
    print('-=' * 10)
    if computador == 1:  # computador PEDRA
        if jogador == 1:
            print('EMPATE!')
            
        elif jogador == 2:
            print(emoji.emojize('VOCÊ GANHOU! :hand:', language='alias'))  # papel
            
        elif jogador == 3:
            print(emoji.emojize('VENCI! PEDRAAAA :punch:', language = 'alias'))  # pedra
    elif computador == 2:  # computador PAPEL
        if jogador == 1:
            print(emoji.emojize('VENCI! PAAAPEL :hand:', language = 'alias'))  # papel
            
        elif jogador == 2:
            print('EMPATE!')
            
        elif jogador == 3:
            print(emoji.emojize('VOCÊ GANHOU!  TESOURAAAA :scissors:', language='alias'))  # tesoura
    elif computador == 3:  # computador TESOURA
        if jogador == 1:
            print(emoji.emojize('VOCÊ GANHOU! PEDRAAAAA :punch:', language='alias'))  # pedra
            
        elif jogador == 2:
            print(emoji.emojize('VENCI!  TESOURAAAA :scissors:', language='alias')) # tesoura
            
        elif jogador == 3:
            print('EMPATE!')                   
    mais = str(input('Quer jogar novamente? S ou N:  '))
    if mais == "N":
        print("Curti muito jogar com você!")
        break
    elif mais == "n":
        print("Curti muito jogar com você!")
        break
    while mais != "N" and mais != "n" and mais != "S" and mais != "s":
        print("Só vale S (sim) ou N (não)")
        mais = str(input('Quer jogar novamente? S ou N:  '))
    if mais == "N":
        print("Curti muito jogar com você!")
        break
    elif mais == "n":
        print("Curti muito jogar com você!")
        break
