from functools import reduce
from math import sqrt, ceil
from exceptions import *


def square_sum(*args):
    if args:
        for arg in args:
            if isinstance(arg, float):
                raise FloatError('Sorry! Floats are not permissioned.')
        try:
            squres = [sqrt(num) for num in args]
            res = reduce(lambda x, y: x + y, squres)
            return ceil(res)
        except TypeError:
            raise StrArgumentError('Sorry! String arguments are not permissioned.')
        except ValueError:
            raise NegativeArgumentError('Sorry! Negative arguments are not permissioned.')
    else:
        raise EmptyArgError("You haven't enter any arguments.")


# print(square_sum())
# print(square_sum(12, 65, 56, 5))
# print(square_sum('d',5))
print(square_sum(12,65,   56  , - 5 ))
# print(square_sum(5, 6.2))
