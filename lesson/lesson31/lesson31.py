# 1. Створити функціонал, який ітеруватиме числа від 1 до 20:
#     - за допомогою класа-ітератора;
#     - за допомогою вираза-генератора (generator expression);
#     - за допомогою функції-генератора (generator function).
#
# 2. Cтворити дві функції, які перевірятимуть, що заданий рядок є паліндромом (читається однаково в обох напрямках,
# без урахування пробілів). Перша функція має використати ітеративний підхід (через цикл), друга - рекурсивний.
#
# 3. Перерахуйте та наведіть приклади якумога більшої кількості варіантів копіювання списку.
#
# 4. Перерахуйте та наведіть приклади якумога більшої кількості варіантів створення словників.
#
# 5. Створіть функцію, яка повертає довжину рядка, отриманого як аргумент.
# До неї створіть декоратор, який явно перетворює аргумент на рядок перед передаванням його задекорованій функції.
# Задекоруйте функцію через виклик декоратора та через синтаксис '@'. Поясніть, що таке декоратор. Завдяки чому можливо використання декораторів?
#
# 6. Створіть клас, на прикладі методов якого покажіть два варіанти декоруання методів класу декоратором property. Поясніть функціонал декоратора property
#
# 7. Наведіть приклади отримання підрядка з рядка за індексами та з використанням об'єкту слайса
#
# 8. Наведіть два приклади варіантів коректної роботи з файлом, коли закриття файлу після читання буде гарантоване
#
# 9. Наведіть приклади двух функцій пошуку елементу у списку. Яку складність має кожен з них? Які обмеження у кожного з них?
#
# 10. Створіть клас, який ілюструє можливіть створення нових об'єктів двома методами: через звичний __init__ та додатковий метод класу.
# Покажіть варіанти використання кожного з них.

# 1. Створити функціонал, який ітеруватиме числа від 1 до 20:
#     - за допомогою класа-ітератора;
#     - за допомогою вираза-генератора (generator expression);
#     - за допомогою функції-генератора (generator function).

class IterNumber:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= self.limit:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


def iter_num(num1, num2):
    while num1 <=num2:
        n = num1
        num1 +=1
        yield n

# 2. Cтворити дві функції, які перевірятимуть, що заданий рядок є паліндромом (читається однаково в обох напрямках,
# без урахування пробілів). Перша функція має використати ітеративний підхід (через цикл), друга - рекурсивний.

def str_iter(string):
    new_str = string.split()
    str_reverse = list(reversed(new_str))
    # if str_reverse == list(string.split()):
    #     return True
    # else:
    #     return False

    count = 0
    while count < len(new_str):
        if new_str[count] == str_reverse[count]:
            return True
        else:
            return False


def str_recurs(string, count=0):
    new_str = string.split()
    print(new_str)
    str_reverse = list(reversed(string.split()))
    print(str_reverse)
    if new_str[count] == str_reverse[count]:
        count += 1
        if count < len(new_str):
            return str_recurs(string, count)
        return True
    else:
        return False



if __name__ == '__main__':
    # iter_num_classs = IterNumber(20)
    # for num in iter_num_class:
    #     print(num)
    # print([num for num in range(1, 21)])
    # iter_n = iter_num(1, 20)
    # print(iter_n)
    # for n in iter_n:
        # print(n)

    # test_str = str_iter('level   level')
    # print(test_str)
    test_rec = str_recurs('lev')
    print(test_rec)