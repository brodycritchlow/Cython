class Cout:
    def __init__(self):
        self.output = ''

    def __lshift__(self, other):

        self.output += str(other)
        print(self.output, end='')

        self.output = ''
        return self
        

class Cin:
    def __init__(self):
        self.input_value = None

    def __lshift__(self, other):
        self.input_value = other

    def __rshift__(self, other):
        if self.input_value is None:
            self.input_value = input(other)
        return self

cout = Cout()
cin = Cin()