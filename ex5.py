import functools
from exceptions import MyTypeError


def checktype(ch_type=None):
    def mydecorator(some_func):
        @functools.wraps(some_func)
        def wrapper(*args):
            for item in args:
                if ch_type is None or isinstance(item, ch_type):
                    some_func(*args)
                # elif ch_type == int and isinstance(item, int):
                #     some_func(*args)
                # elif ch_type == float and isinstance(item, float):
                #     some_func(*args)
                # elif ch_type == str and isinstance(item, str):
                #     some_func(*args)
                # elif ch_type == list and isinstance(item, list):
                #     some_func(*args)
                # elif ch_type == tuple and isinstance(item, tuple):
                #     some_func(*args)
                # elif ch_type == set and isinstance(item, set):
                #     some_func(*args)
                # elif ch_type == dict and isinstance(item, dict):
                #     some_func(*args)
                else:
                    raise MyTypeError('Type of function\'s argument is not valid!')

        return wrapper

    return mydecorator


@checktype(list)
def myfunc(n):
    print(n)


myfunc([2, 5])
