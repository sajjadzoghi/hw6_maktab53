class EmptyArgError(Exception):
    pass


class StrArgumentError(EmptyArgError):
    pass


class NegativeArgumentError(EmptyArgError):
    pass


class FloatError(EmptyArgError):
    pass


class MyTypeError(EmptyArgError):
    pass
