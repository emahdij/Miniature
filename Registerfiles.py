class registers:
    __register = []

    def __init__(self):
        self.register = [0] * 16

    def getregister(self, i):
        return self.register[i]

    def setregister(self, i, x):
        self.register[i] = str(x)

    def registers(self):
        return self.register
