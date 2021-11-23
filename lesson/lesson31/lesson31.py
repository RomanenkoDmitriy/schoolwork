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
        num1 += 1
        yield n

# 2. Cтворити дві функції, які перевірятимуть, що заданий рядок є паліндромом (читається однаково в обох напрямках,
# без урахування пробілів). Перша функція має використати ітеративний підхід (через цикл), друга - рекурсивний.

def str_iter(string):
    new_str = string.strip()
    str_reverse = list(reversed(new_str))
    count = 0
    while count < len(new_str):
        if new_str[count] == str_reverse[count]:
            return True
        else:
            return False

    # if str_reverse == list(string.split()):
    #     return True
    # else:
    #     return False


def str_recurs(string: str, count=0):
    new_str = list(string.strip())
    # print(new_str)
    str_reverse = list(reversed(string))
    # print(str_reverse)
    if new_str[count] == str_reverse[count]:
        count += 1
        if count < len(new_str):
            return str_recurs(string, count)
        return True
    else:
        return False


# 3. Перерахуйте та наведіть приклади якумога більшої кількості варіантів копіювання списку.
l = [1, 2, 3]
l2 = l.copy()

l3 = [val for  val in l]

l4 = l[:]

# 4. Перерахуйте та наведіть приклади якумога більшої кількості варіантів створення словників.
dict1 = {str(val): (val + 1) for val in range(5)}

dict12 = {'a': 1, 'b': 2, 'd':3}

list_key = ['a', 'b', 'd']
list_val = [1, 2, 3]
dict3 = dict(zip(list_key, list_val))

# 5. Створіть функцію, яка повертає довжину рядка, отриманого як аргумент.
# До неї створіть декоратор, який явно перетворює аргумент на рядок перед передаванням його задекорованій функції.
# Задекоруйте функцію через виклик декоратора та через синтаксис '@'. Поясніть, що таке декоратор. Завдяки чому можливо використання декораторів?

def decor_str(func):
    def wrapper(string):
        new_str = str(string)
        return func(new_str)
    return wrapper

@decor_str
def some_func(string):
    return len(string)

some_func = decor_str(some_func)

# Декоратор это функция меняющая поведение другой функции
# Декораторы можно использовать благодаря тому что функция это обьект первого порядка


# 6. Створіть клас, на прикладі методов якого покажіть два варіанти декоруання методів класу декоратором property. Поясніть функціонал декоратора property

class SomeClass:

    def __init__(self, val):
        self._val = val

    @property
    def val(self):
        return self._val

    def mu_val(self):
        return self._val

    property(mu_val)

# property позволяет упровлять атрибутами класса


# 7. Наведіть приклади отримання підрядка з рядка за індексами та з використанням об'єкту слайса
some_str = 'some string'
index_str = f'{some_str[0]}{some_str[1]}{some_str[2]}{some_str[3]}'
slice_str = some_str[:4]


# 8. Наведіть два приклади варіантів коректної роботи з файлом, коли закриття файлу після читання буде гарантоване
path = '#'
file = open(path, 'r')
file.close()
with open(path, 'r') as file:
    pass


# 9. Наведіть приклади двух функцій пошуку елементу у списку. Яку складність має кожен з них? Які обмеження у кожного з них?
#  Можно применять если елементы в листе упорядочены, сложность логорифмическая
some_list = [1, 2, 3, 4]
element = 3

def binary(some_list, element, l=None, m=None):
    if l is None and m is None:
        l = 0
        m = len(some_list) - 1

    if l <= m:
        mid = len(some_list) // 2

        if some_list[mid] == element:
            return some_list[mid]
        elif some_list[mid] > element:
            return binary(some_list, element, l, mid-1)
        else:
            return binary(some_list, element, mid+1, m)
    else:
        return False

# сложность O(n)
def mu_search(some_list, elevent):
    for val in some_list:
        if val == elevent:
            return val

# 10. Створіть клас, який ілюструє можливіть створення нових об'єктів двома методами: через звичний __init__ та додатковий метод класу.
# Покажіть варіанти використання кожного з них.
class MyClass:

    def __init__(self, val):
        self.val = val

    @classmethod
    def add_atr(cls, val):
        obj = cls(val=val)
        return obj


# some_class = MyClass(1)
# print(some_class.val)
# new_class = MyClass.add_atr(2)
# print(new_class.val)

# Розробити програму, яка на вхід отримуватиме суму як число з плаваючою точкою (наприклад, 1787.80) і повертариме словники,
# який репрезентує найменшу кількість купюр і монет, що ходять в Україні, які потрібні для того, щоб набрати таку суму
# {1000: 1, 500:1, 200: 1, 50:1, 10: 3, 5: 1, 2: 1}, {50:1, 10:3}

def my_cashbox(cash):
    cash_list = [1000, 500, 200, 50, 10, 5, 2, 1, 0.5, 0.1]
    some_dict = {}
    item = 1
    count = 0
    while cash:
        if cash_list[count] <= cash:
            some_dict[str(cash_list[count])] = item
            cash = round(cash - cash_list[count], 1)
            item += 1
        else:
            count += 1
            item = 1
    return some_dict

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
    # test_rec = str_recurs('level  level')
    # print(test_rec)
    # print(some_func('qqqq'))
    # some_class = MyClass(1)
    # some_class.add_atr('val2', 2)
    # print(some_class.val2)
    item = my_cashbox(1787.80)
    print(item)