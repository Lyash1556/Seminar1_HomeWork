# Задача 2: Найдите сумму цифр трехзначного числа.
n = int(input('Input number: '))
sum = 0
while n > 0:
    t = n % 10
    sum = sum + t
    n = n // 10
print(f'The sum of the digits in a number is: {sum}')