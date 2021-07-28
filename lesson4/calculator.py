class P:
    def add(self, *args):
        return sum(args)


class M:
    def sub(self, a, b):
        self.a = a
        self.b = b
        return a -b


class D:
    def div(self, a, b):
        self.a = a
        self.b = b
        return a / b


class U:
    def mult(self, a, b):
        self.a = a
        self.b = b
        return a * b
