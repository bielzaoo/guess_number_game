"""
Joguinho: Advinhe o número correto!
"""

import random
import os

limit = input('Deseja definir um limite?: ')
if limit.lower() == 's' or limit.lower() == 'sim':
    begnning = input('Vai de: ')
    final = input('Até: ')
    try:
        begnning = int(begnning)
        final = int(final)
        correct_number = random.randint(begnning,final)
        
    except ValueError:  # Para evitar que o programa gere erros indesejados.
        print('[Por favor, insira apenas números inteiros!]')
        exit(-1)

correct_number = random.randint(1,10)
guess_number = None
number_already_inserted = []    # Um "buffer" para segurar o númeris ja escolhidos pelo user.

while guess_number != correct_number:
    if len(number_already_inserted) == 0:
        print('[Você ainda nçao escolheu um número]')
    else:
        print('--== Números já escolhidos ==--')
        for number in number_already_inserted:
            print(f'X {number}')
    guess_number = input('Tente acertar o númeor correto: ')
    
    try:
        guess_number = int(guess_number)
        number_already_inserted.append(guess_number)
    except ValueError:  # # Para evitar que o programa gere erros indesejados.
        os.system('cls')
        print('[Por favor, digite apenas números inteiros!]')
        continue

    if guess_number == correct_number:
        print(f'[+] Parabéns! Você acertou!')
    else:
        os.system('cls')
        print('[!!!] Errou, tente novamente! :( ')
        print()