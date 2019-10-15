__author__ = 'kwilliam'


def addition(a, b):
    c = a + b
    return c


class Calculator:
    result = ''

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result
