# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
# на два прямоугольника).

n = int(input('input the length of the chocolate bar: '))
m = int(input('input the width of the chocolate bar: '))
k = int(input('input the number of pieces: '))
if((k % n == 0 or k % m == 0) and k <= n * m):
    print(f'You can take {k} pieces from this chocolate bar with one break.')
else: print(f'You can not take {k} pieces.')