from exceptions import FloatError, MyTypeError
from functools import reduce

try:
    li = eval(input())
    for item in li:
        if isinstance(item, float):
            raise FloatError('Sorry! Floats are not permissioned.')
    print('max=', reduce(lambda x, y: max(x, y), li))
    print('min=', reduce(lambda x, y: min(x, y), li))
except (NameError, TypeError):
    raise MyTypeError('Sorry! All arguments should be only integers!')

# [566,2,5 ,    56,47 ,   8]
# 566,2,-  5 ,  56,47 ,   8
# [566,2,5 ,    56,47 ,  "d"]
