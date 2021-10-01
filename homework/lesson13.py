def my_decorator(*args, **kwargs):
    def internal_function(func):
        def wrapper():
            print(*args, **kwargs)
            print('before')
            func()
            print('after')
        return wrapper
    return internal_function

@my_decorator('Arg1', 'Arg2')
def hello_world():
    print('Hello World')



def my_decorator2(val, *args):
    def internal_function(func):
        def wrapper(*arg):
            func(*arg)
            for name in args:
                func(name)
            print(val, '\n__________________________________')
            print(*args)
        return wrapper
    return internal_function


@my_decorator2('Уря сработало!!!', 'World', 'Bob', 'Joi')
def hello(name):
    print(f'Hello {name}!')


if __name__ == '__main__':
    hello_world()
    print('<--------------------------------------------------------------------------------------------------->')
    hello('Eva')
