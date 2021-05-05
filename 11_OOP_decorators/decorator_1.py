def uppercase_decorator(func):
    def wrapper():
        # txt = func()
        # txt = txt.upper()
        # return txt
        return func().upper()
    return wrapper


@uppercase_decorator
def lorem_generator():
    return 'lorem ipsum dolor sit amet'


print(lorem_generator())
