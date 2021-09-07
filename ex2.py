# Solution1:
# def remove_none(li):
#     return list(filter(lambda x: x != None, li))
#
# print(remove_none([1, None, "hi", 55, -9, None, None, 1.1]))


# Solution2:
from exceptions import EmptyArgError


def remove_none(*args):
    if args:
        for item in args:
            if isinstance(item, list):
                return list(filter(lambda x: x is not None, item))
        return list(filter(lambda x: x is not None, args))
    else:
        raise EmptyArgError("You haven't enter any arguments.")
        # None


print(remove_none([1, None, "hi", 55, -9, None, None, 1.1]))
print(remove_none(1, None, "hi", 55, -9, None, None, 1.1))
print(remove_none())
