def morning(func):
    def wrapper(args_for_function):
        func(args_for_function)
        print('Good morning,', args_for_function)
    return wrapper

@morning
def greetings(name):
    print('Hello,', name)

