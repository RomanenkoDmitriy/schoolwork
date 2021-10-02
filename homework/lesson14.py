def my_decorator(func):
    def wrapper(self):
        print('Decorator')
        return func(self)
    return wrapper


class Hello:

    @my_decorator
    def hello_world(self):
        return 'Hello world!'

if __name__ == '__main__':

    hello = Hello()
    print(hello.hello_world())

