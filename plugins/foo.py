class Foo:
    def __init__(self, n):
        self.n = n ** n
    
    def output(self):
        print('Class Foo: {}'.format(self.n))


def plugin(n):
    return Foo(n)
