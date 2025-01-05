import random

print('\n'
      'Добро пожаловать в игру "Угадай число"!\n'
      '\n'
      'В игре доступно три уровня сложности:\n'
      '\n'
      'Сопляк - Вам нужно угадать число от 1 до 10 за 4 попытки!\n'
      'Чиловый парень - Вам нужно угадать число от 1 до 50 за 5 попыток!\n'
      'Ты кем себя возомнил ?! - Вам нужно угадать число от 1 до 1000 за 10 попыток!'
      )
print('-----------------------------------')

# Глобальные счетчики
wins = 0
losses = 0


def choose_difficulty():
    """Функция выбора уровня сложности."""
    complexity = input('Введите "первая", "вторая" или "третья": ').lower()
    if complexity == 'первая':
        return 1, 10, 4
    elif complexity == 'вторая':
        return 1, 50, 5
    elif complexity == 'третья':
        return 1, 1000, 10
    else:
        print('Некорректный ввод. Устанавливается уровень "Чиловый парень".')
        return 1, 50, 5


def game():
    """Функция основной игры."""
    global wins, losses
    range_min, range_max, attempts = choose_difficulty()
    M = random.randint(range_min, range_max)

    print(f'Угадайте число от {range_min} до {range_max}. У вас {attempts} попыток.')
    count = 0

    while count < attempts:
        try:
            num = int(input('Введите число: '))
            if num < range_min or num > range_max:
                print(f'Число должно быть в диапазоне от {range_min} до {range_max}, Недотёпа. Попытка не засчитывается.')
                continue
            if num == M:
                print('Мои поздравления!')
                wins += 1
                break
            elif num < M:
                print('Больше')
            else:
                print('Меньше')
            count += 1
        except ValueError:
            print('Пожалуйста, вводите целое число.')
            continue
    else:
        print(f'YOU DIE!\nЗагаданное число было: {M}')
        losses += 1

    print(f'Счет: Побед — {wins}, Поражений — {losses}')


# Основной цикл игры
while True:
    game()
    play_again = input('Хотите сыграть еще раз? (да/нет): ').lower()
    if play_again not in ['да', 'yes']:
        print(f'Итоговый счет: Побед — {wins}, Поражений — {losses}. До свидания!')
        break