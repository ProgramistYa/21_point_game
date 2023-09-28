"""
Игра 21 очко с ботом, сначала по правилам играем мы,
потом тянет карту бот.
"""
import random
import os
import time

deck = [2, 3, 4, 6, 7, 8, 9, 10, 11] * 4
random.shuffle(deck)
print('Поиграем в 21 очко?')
count = 0
count_bota = 0
while True:
    choice = input('Будете брать карту? y/n\n')
    if choice == 'y':
        contine = deck.pop()
        print('Вам попалась карта достоинством %d' %contine)
        count += contine
        if count > 21:
            print('Вы проиграли', count)
            break
            #continue
        elif count == 21:
            print('Поздравляю у вас очко(21)')
        else:
            print('У вам %d очков' %count)
    if choice == 'n':
        print('У вас %d очков.' %count)
        print('Теперь ходит бот')
        # Ход бота
        while True:
            if count_bota <= 15:
                print("Бот берет карту")
                score_carts = random.choice(deck)
                print("--------------------")
                print("Боту выпало", score_carts, "очков.")
                count_bota += score_carts
                print("--------------------")
                print("У бота ", count_bota, "очков.")
                time.sleep(4)
                continue
            if count_bota > 21:
                print("Бот проиграл.\nТак как у него", count_bota, "очков, а у вас ", count)
                input("Нажмите Enter, чтобы закрыть");
                exit(0)
            if count_bota > count:
                print("Бот победил.\nТак как у него", count_bota, "очков, а у вас ", count,
                      "\nНе растраивайтесь. Попробуйте ещё раз.")
                input("Нажмите Enter, чтобы закрыть");
                exit(0)
            if count_bota == count:
                print("Вы набрали равное количество очков и у вас ничья")
            break
print('Заходите к нам еще!')
