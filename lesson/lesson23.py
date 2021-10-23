
#


#

#

#

#

#

#
#

#
#
#

#
# 12. Викликати кожну задекоровану функцію з завдання 11 з аргументами:
#     1) a = 30, b = 6
#     2) a = 100, b = 1
#     3) a = 999, b = 9
#     4) a = 4, b = 1024
#
#     Навести результат виконання задекорованих функцій, зробити висновок про швидкість роботи кожної з задекорованих функцій.


# 1. Чи правильне твердження, що Python - нетипізована мова програмування? Наведіть приклад коду,
# який підтвердить або спростує це твердження.
#Утверждение не вено
val = 'some string'
val1 = 3
# TupeEror
#print(val + val1)


# 2. Яка різниця між мутебальними та імутабельними типами даних у Python? Наведіть короткий приклад коду,
# який ілюструє цю різницю
# В мутабельных обект после создания можно  изменить а в имутабельных нет
list1 = list2 = [1, 2, 3, 4]
# print(list1)
# print(list2)
list2[1] = 5
# print(list1)
# print(list2)

str1 = str2 = 'hello'
# print(id(str1))
# #str2[2] = 'a'
# print(str2)
# srt2 = f'H{str2[1:]}'
# print(srt2)
# print(id(srt2))

# 3. У чому полягає принцип "duck typing"? Наведіть приклад застосування цього принципу
#Если какойто обект ходит как утка и крякает как утка то это утка
some_int = 5
some_now_int = some_int * 3
# print(some_now_int)

some_string = 'text'
some_now_string = some_string * 3
# print(some_now_string)

# 4. Які типи даних можуть бути ключами у dict?
#неизменяемые обьекты

# 5. У чому полягає різниця між set та frozen set?
#set - мутабельный,  frozen set - имутабельный

# 6. Перерахуйте основні принципи ООП.
# наследование
# инкапсуляция
# полиморфизм

# 7. Наведіть приклад коду, який демонструє принцип спадкування
class Animal:
    def vois(self):
        print('May')

class Cat(Animal):
    pass

cat = Cat()
# cat.vois()

# 8. Створіть декоратор, який заміряє час виконання задекорованої функції. Декоратор не обмежує кількість та порядок аргументів, що передаються функції.
# Декоратор має у циклі викликати задекоровану функцію 1000 разів, а після того виводити рядок з назвою функції,
# її аргументами, часом виконання 1000 викликів. Декоратор має повертати результат останнього, тисячного, виклику функції.

import time
def time_decor(func):
    def wrapper(*args):
        start_time = time.time()
        for inem in range(1000):
            func(*args)
        print(f'{func.__name__} {args} {time.time() - start_time}')
        return func(*args)
    return wrapper


@time_decor
def hello(name):
    return f'Hello {name}!'


#print(hello('Bob'))

#9. Реалізувати функцію eucledian_gcd(a: int, b: int) -> int, яка обраховуватиме найбільший спільний дільник для агрументів a та b за алгоритмом Евкліда.

# Алгоритм Евкліда для пошуку НСД:
#     1) Допоки a != b:
#         - якщо a > b, то a = a - b
#         - якщо b > a, то b = b - a
#     2) Коли a == b, повертаємо а, яке і буде найбільшим спільним дільником.

def eucledian_gcd(a: int, b: int) -> int:
    if a == b:
        return a
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
# print(eucledian_gcd(33, 17))

# 10. З модулю math імпортувати функцію gcd, яка обраховує набільший спільний дільник.
import math
# print(math.gcd(33, 17))

# 11. Задекорувати функції з завдань 9 та 10 декоратором з завдання 8.

@time_decor
def eucledian_gcd1(a: int, b: int) -> int:
    if a == b:
        return a
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# print(eucledian_gcd1(12, 4))

@time_decor
def math_gsd_main(a: int, b: int) -> int:
    return math.gcd(a, b)

# print(math_gsd_main(12, 4))

# 12. Викликати кожну задекоровану функцію з завдання 11 з аргументами:
#     1) a = 30, b = 6
#     2) a = 100, b = 1
#     3) a = 999, b = 9
#     4) a = 4, b = 1024

@time_decor
def eucledian_gcd11(a: int, b: int) -> int:
    if a == b:
        return a
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(eucledian_gcd11(30, 6))
print(eucledian_gcd11(100, 1))
print(eucledian_gcd11(999, 9))
print(eucledian_gcd11(4, 1042))

@time_decor
def math_gsd_main11(a: int, b: int) -> int:
    return math.gcd(a, b)

print('______________________________________________')
print(math_gsd_main11(30, 6))
print(math_gsd_main11(100, 1))
print(math_gsd_main11(999, 9))
print(math_gsd_main11(4, 1042))