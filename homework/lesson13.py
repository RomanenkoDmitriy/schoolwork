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


hello_world()