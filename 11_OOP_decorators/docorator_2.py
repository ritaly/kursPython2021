from time import process_time, sleep


def timepassed(func):
    def nested():
        start = process_time()
        func()
        end = process_time()
        result = end - start
        print(result)
    return nested


@timepassed
def example_function():
    print('Start')
    sleep(5)
    print('Koniec')

@timepassed
def example_2():
    var = 4+5
    return var * 40



example_2()
