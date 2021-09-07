from functools import reduce


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibs_until(num):
    i = 1
    while fib(i) < num:
        yield fib(i)
        i += 1


mygener = fibs_until(18)
odds = list(filter(lambda x: x % 2 != 0, mygener))
print(reduce(lambda x, y: x + y, odds))
