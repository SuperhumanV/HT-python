import random
  


def yes_no() -> bool:
    while True:
        answer = input('Y or N?\n').lower()
        if answer == 'y' or answer == 'yes':
            return True
        elif answer == 'n' or answer == 'no':
            return False
        else:
            print('Invalid input')

def bot():
    print('\033[33m{}\033[0m'.format('Вы хотите играть с ботом?'))
    return yes_no()
    

def Start():
    global player_1
    global player_2
    global ask
    global hard_level
    global total_candies
    global take_candies
    global max_candies
    global take_candies
    global player_candies
    global bot_candies
    total_candies = int(input('\033[36m{}\033[0m'.format('Введите максимальное количество конфет ')))
    take_candies = 0
    player_candies = 0
    max_candies = int(input('\033[36m{}\033[0m'.format('Максмальное число конфет за одни ход: ')))
    bot_candies = 0
    print('\033[32m{}\033[0m'.format(f'Конфет лежит: {total_candies} , задача игроков - брать конфеты по очереди, но не более, чем {max_candies} за один ход. Тот, после чьего хода на столе не останется конфет - победит '))
    ask =bot()
    if ask == False:
        player_1 = input('\033[36m{}\033[0m'.format('Введите имя первого игрока '))
        player_2 = input('\033[36m{}\033[0m'.format('Введите имя второго игрока '))
    else:
        player_1 = input('\033[36m{}\033[0m'.format('Введите имя игрока '))
        hard_level = int(input('\033[33m{}\033[0m'.format(f'Выберите цифру уровня сложности: 1.Easy, 2.Medium, 3.Hard ')))
    player_turn()

def player_turn():
    global player_1
    global player_2
    global total_candies
    global take_candies
    global player_candies
    global bot_candies
    
    print('\033[33m{}\033[0m'.format(f'Ход игрока {player_1}, конфет на столе: {total_candies}'))
    take_candies = int(input('\033[36m{}\033[0m'.format(f'Сколько конфет возьмете? ')))
    while take_candies>(max_candies + 1) or take_candies<1 or take_candies>total_candies:
        print('\033[31m{}\033[0m'.format(f'Столько конфет не унести'))
        take_candies = int(input('\033[36m{}\033[0m'.format(f'Сколько конфет возьмете?')))
    total_candies-=take_candies
    player_candies+=take_candies
    if total_candies>0:
        if ask == True : bot_turn()
        else: player_2_turn()
    else:
        print('\033[32m{}\033[0m'.format(f'Шуршим фантиками. Это победа игрока {player_1}!'))
def player_2_turn():
    global total_candies
    global take_candies
    global player_candies
    global bot_candies
    print('\033[33m{}\033[0m'.format(f'Ход игрока {player_2}, конфет на столе: {total_candies} '))
    take_candies = int(input('\033[36m{}\033[0m'.format(f'Сколько конфет возьмете? ')))
    while take_candies>(max_candies + 1) or take_candies<1 or take_candies>total_candies:
        print('\033[31m{}\033[0m'.format('Столько конфет не унести'))
        take_candies = int(input('\033[36m{}\033[0m'.format(f'Сколько конфет возьмете?')))
    total_candies-=take_candies
    player_candies+=take_candies
    if total_candies>0:
        player_turn()
    else:
        print('\033[32m{}\033[0m'.format(f'Шуршим фантиками. Это победа игрока {player_2}!'))
def bot_turn():
    global hard_level
    global total_candies
    global take_candies
    global player_candies
    global bot_candies
    print('\033[33m{}\033[0m'.format(f'Ход бота, на столе осталось {total_candies} конфет'))
    if hard_level == 1:
        take_candies = random.randint(1, max_candies)
    elif hard_level == 2:
        if random.randint(0, 1):
            move = total_candies % (max_candies + 1)
            if move == 0:
                take_candies = random.randint(1, max_candies)
            else:
                take_candies= total_candies %(max_candies + 1)
        else:
            take_candies = random.randint(1, max_candies)
    elif hard_level == 3:
        take_candies = total_candies % (max_candies + 1) if total_candies % (max_candies + 1) !=0 else random.randint(1, max_candies)
    total_candies-=take_candies
    bot_candies+= take_candies
    print('\033[31m{}\033[0m'.format(f'Бот съел конфет: {take_candies} '))
    if total_candies>0:
        player_turn()
    else:
        print('\033[31m{}\033[0m'.format('Бот съел все конфеты'))
        print('\033[36m{}\033[0m'.format('Хотите сыграть еще раз?'))
        ask = yes_no()
        if ask == True:
            Start()
        else:
            print('\033[32m{}\033[0m'.format('У нас еще много конфет, возвращайтесь!'))

Start()