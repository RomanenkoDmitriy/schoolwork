#Написати функцію, яка отримуватиме як агрументи список цілих чисел numbers і ціле числе p, 
# та повертає новий список, де кожен елемент дорівнює відповідному елементу з початкового списку у ступіні p.

import random

numbers = list(range(2,10))
number = random.randint(2, 5)

def degree_numbers(list_numbers, degree):
    return [pow(num, degree) for num in list_numbers]

dict_degree_numbers = degree_numbers(numbers, number)
print(dict_degree_numbers)

