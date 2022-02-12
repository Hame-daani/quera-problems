class Chain:
    def __init__(self, x):
        if type(x) in [str, int, float]:
            self.x = x
        else:
            raise Exception('invalid operation')

    def __call__(self, y=None):
        if type(y) == str and type(self.x) == str:
            return Chain(self.x + " " + y)
        if type(y) in [int, float] and type(self.x) in [int, float]:
            return Chain(self.x + y)
        raise Exception('invalid operation')

    def __eq__(self, __o: object):
        return self.x == __o

    def __repr__(self):
        if type(self.x) == str:
            return f"'{self.x}'"
        return f"{self.x:g}"
