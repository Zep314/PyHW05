# Создайте программу для игры в ""Крестики-нолики"".

import botAI

# Хранить все будем в одномерном массиве
field = '123456789'

def PrintField(local_field): # функция печати состояния игрового поля
    print('-' * 13)
    for i in range(3): # печатаем целыми строками
        print(f'| {local_field[i*3]} | {local_field[i*3 + 1]} | {local_field[i*3 + 2]} |')
        print('-' * 13)

def MyInput(local_field): # функция ввода нового элемента (с проверками)
    num = int(input('Введите позию, куда хотите сходить 1..9: ')) # проверку на нецифру делать не стал
    while True:
        if not ((0 < num) and (num < 10)):
            print('Ввели неправильное место на поле')
        elif not(local_field[num-1] in '123456789'): # если поле занято, то вместо цифры там X или O
            print('Это поле уже занято')
        else: return str(num)
        num = int(input('Введите позицию, куда хотите сходить 1..9: '))

def MyCheckGame(local_field): # функция проверки окончания игры
    win_patterns = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)) # если в этих позициях
                                                                                     # стоят XXX или OOO,
                                                                                     # то кто-то выйграл
    if len(local_field.replace('X','').replace('O','')) == 0: return 'Победила дружба! Ничья!'
    if 'XXX' in list(filter(lambda x: x,[local_field[win_patterns[i][0]]+\
                                         local_field[win_patterns[i][1]]+\
                                         local_field[win_patterns[i][2]] \
                                    for i in range(len(win_patterns))])):
        return 'XXX Победили крестики XXX'
    if 'OOO' in list(filter(lambda x: x,[local_field[win_patterns[i][0]]+\
                                         local_field[win_patterns[i][1]]+\
                                         local_field[win_patterns[i][2]] \
                                    for i in range(len(win_patterns))])):
        return 'OOO Победили нулики OOO'
    return 'None'

print(' Крестики - нолики (Игра с ИИ)')
game_result = 'None'
#x_turn = True # Х - ходят первые

# настройка игры - изначальный выбор параметров
x_turn = (True if input("X - ходят первые? [y/n] ") == 'y' else  False)
bot_play_X = (False if input("Бот играет за 0? [y/n] ") == 'y' else True)

print("Выберите алгоритм игры бота:")
print(f"\t1. Самый тупой")   # 1 - тупо выбирает первую свободную ячейку
print(f"\t2. Случайный")     # 2 - случайно выбирает одну из свободных ячеек
print(f"\t3. Непобедимый")   # 3 - считает все поле, не может проиграть
bot_algorithm = int(input("Номер алгоритма (1, 2 или 3): "))

while game_result == 'None':
    PrintField(field)
    if x_turn:
        print('Ходят X')
        if bot_play_X:
            field = field.replace(botAI.get_bot_turn(field,'X',bot_algorithm),'X') # бот сходил за X
        else:
            field = field.replace(MyInput(field),'X') # чел сходил за X
    else:
        print('Ходят O')
        if not bot_play_X:
            field = field.replace(botAI.get_bot_turn(field,'O',bot_algorithm),'O') # бот сходил за O
        else:
            field = field.replace(MyInput(field),'O') # чел сходил за O    game_result = MyCheckGame(field)
    game_result = MyCheckGame(field)  # проверяем, чего там с результатом игры
    x_turn = not x_turn

print('Игра окончена')
PrintField(field)
print(game_result)
