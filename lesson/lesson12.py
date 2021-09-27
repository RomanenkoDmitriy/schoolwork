import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        call_time = time.localtime()
        try:
            func(*args, **kwargs)
        except RuntimeError as e:
            print(str(e))
        print(f'Call time: {call_time}\nName function: {func.__name__}\nArguments: {[x for x in args]}')
    return wrapper


@my_decorator
def my_func(num):
    if num % 2:
        raise RuntimeError('Just for fun!')
    else:
        print(num)

@my_decorator
def sum_two_number(a, b):
    print(a + b)



#my_func = my_decorator(my_func)
my_func(3)
print('--------------------------------------------------------')
sum_two_number(2, 3)
