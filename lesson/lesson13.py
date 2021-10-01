def log(func):
    def wrapper(*args):
        print(f'Argyments: {args}\nResult: {func(*args)}')
        return func(*args)
    return wrapper

@log
def sum_two_numbers(a, b):
    return a + b

# sum_two_numbers(1, 2)
# sum_two_numbers(3, 2)
# sum_two_numbers(16, 24)
s = sum_two_numbers(11, 22)

print(s)