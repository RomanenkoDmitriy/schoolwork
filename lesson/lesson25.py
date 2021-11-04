#
# 1. Якщо ми запишемо всі натуральні числа, що кратні 3 або 5, та менші 10, ми отримаємо 3, 5, 6 та 9. Сума цих чисел буде дорівнювати 23.
# Знайти суму всіх чисел, що кратні 3 або 5, та менші 1000.
#
# 2. Для числа 13195 існують такі прості дільники (прості числа, на яке задане число ділиться без залишку):
# 5, 7, 13, 29. Знайти найбільший простий дільник числа 600851475143.
#
# 3. 2520 найменше число, що ділиться на будь-яке число від 1 до 10 без залишку.
# Яке найменше позитивне число ділиться без залишку на всі числа від 1 до 20?
#
# 4. Триплет Піфагора - це набір з трьох натуральних чисел a < b < c, для якого a**2 + b**2 = c**2. Наприклад,  3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# Існує тільки один триплет Піфагора, для якого a + b + c = 1000. Знайти добуток a*b*c лдя цього триплету.
#
# 5. Сумою простих чисел менших 10 є 2 + 3 + 5 + 7 = 17. Знайти суму всіх простих чисел, менших за 2 мільйони.
#
#
# Примітка:
# Натуральні числа - всі цілі числа більші 0.
# Прості числа - такі натуральні числа, які мають тільки два натуальних дільники: 1 та саме це число.

# 1. Якщо ми запишемо всі натуральні числа, що кратні 3 або 5, та менші 10, ми отримаємо 3, 5, 6 та 9. Сума цих чисел буде дорівнювати 23.
# Знайти суму всіх чисел, що кратні 3 або 5, та менші 1000.

sum_nam = [num for num in range(1000) if num % 3 == 0 or num % 5 == 0]
# print(sum(sum_nam))

# 2. Для числа 13195 існують такі прості дільники (прості числа, на яке задане число ділиться без залишку):
# 5, 7, 13, 29. Знайти найбільший простий дільник числа 600851475143.
number = 600851475143
# divider_num = [num for num in range(number -, 600800000000, -1) if number % num == 0]
# divider_num = []
# for num in range(number - 1, number - 100000000, -1):
#     if number % num == 0:
#         divider_num.append(num)
# print(divider_num)

# 3. 2520 найменше число, що ділиться на будь-яке число від 1 до 10 без залишку.
# Яке найменше позитивне число ділиться без залишку на всі числа від 1 до 20?

for range_num in range(1, 1000000):
    if range_num % range(1, 21) == 0:
        print(range_num)





# 4. Триплет Піфагора - це набір з трьох натуральних чисел a < b < c, для якого a**2 + b**2 = c**2. Наприклад,  3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# Існує тільки один триплет Піфагора, для якого a + b + c = 1000. Знайти добуток a*b*c лдя цього триплету.

# for a in range(1, 497):
#     for b in range(2, 498):
#         for c in range(3, 500):
#             if (a < b < c) and a**2 + b**2 == c**2 and\
#                     a + b + c == 1000:
#                 print(a, b, c)


# 5. Сумою простих чисел менших 10 є 2 + 3 + 5 + 7 = 17. Знайти суму всіх простих чисел, менших за 2 мільйони.
# Примітка:
# Натуральні числа - всі цілі числа більші 0.
# Прості числа - такі натуральні числа, які мають тільки два натуальних дільники: 1 та саме це число.

numbers_list = [num for num in range(1, 2000001) if num % 1 == 0 and num % num == 0]
# print(sum(numbers_list))