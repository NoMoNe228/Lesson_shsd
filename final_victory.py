from victory import igra


def answw():
    ans = str(input('Ты готов начать игру? 1 - Готов, 2 - Не готов'))
    if ans == '1':
        igra()
    elif ans == '2':
        print("Жаль, увидимся позже!")
    else:
        print('Пожалуйста, введи число 1 или 2')
        answw()