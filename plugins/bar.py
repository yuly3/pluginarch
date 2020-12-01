class Bar:
    def __init__(self, n):
        self.n = n
    
    def output(self):
        print('Class Bar: {}'.format(self.n))


def plugin(n):
    return Bar(n)
