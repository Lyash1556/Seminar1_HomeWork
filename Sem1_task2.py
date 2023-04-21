# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?


s = int(input('how many cranes did the children make?: '))
if s % 6 == 0:
    print(f'Peter made {int(s / 6)} cranes.\nSergey made {int(s / 6)} cranes.\nKatya made {int((s / 3) * 2)} cranes.')
else:
    print('Quantity is not correct!')