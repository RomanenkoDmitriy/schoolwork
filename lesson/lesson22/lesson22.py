def linear_shift(array: list, shift: int) -> list:
    '''
    array = [1, 2, 3, 4] shift = 1 => [0, 1, 2, 3]
    array = [1, 2, 3, 4] shift = 2 => [0, 0, 1, 2]
    array = [1, 2, 3, 4] shift = 3 => [0, 0, 0, 1]
    '''
    num_list = []
    #for item in range(shift - 1):
    for num in array:
        numbers = num - shift
        if numbers <= 0:
            num_list.append(0)
        else:
            num_list.append(numbers)
    return num_list


#print(linear_shift([1, 2, 3, 4], 3))



def circular_shift(array: list, shift: int) -> list:
    '''
    array = [1, 2, 3, 4] shift = 1 => [4, 1, 2, 3]
    array = [1, 2, 3, 4] shift = 2 => [3, 4, 1, 2]
    array = [1, 2, 3, 4] shift = 3 => [2, 3, 4, 1]
    '''
    for item in range(shift):
            array.insert(0, (array.pop(-1)))
    return array
print(circular_shift([1, 2, 3, 4], 1))


def nested_parentheses(incoming: str) -> bool:
    '''
    Функція отримує рядок, який складається тільки зі знаків "(" або ")"
    Рядок вважається таким, що містить коректно вкладені скобки, якщо для
    кожної скобки "(" існує відповідна ")".
    Функція повертає булевську змінну, яка показує, чи містить вхідний рядок
    тільки правильно вкладені скобки - True, чи ні - False
    incoming = "((())(())())" => True
    incoming = "" => True
    incoming = "(((())))" => True
    incoming = "())" => False
    incoming = "(()()(())" => False
    '''


    s = []
    balanced = True
    index = 0
    while index < len(incoming) and balanced:
        token = incoming[index]
        if token == "(":
            s.append(token)
        elif token == ")":
            if len(s) == 0:
                balanced = False
            else:
                s.pop()

        index += 1

    return balanced and len(s) == 0


print(nested_parentheses('((())(())())'))
print(nested_parentheses(''))
print(nested_parentheses('(((())))'))
print(nested_parentheses('())'))
print(nested_parentheses('(()()(())'))