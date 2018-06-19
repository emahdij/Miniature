class DataMem:
    arr = [''] * 16 * 1024

    # def __init__(self):
    #     self.arr = [""] * 16 * 1024

    def get(self, i):
        return self.arr[int(i)]

    def set(self, i, x):
        self.arr[int(i)] = str(x)

    def printMem(self):
        for i in range(len(self.arr)):
            if self.arr[i] != '':
                print("Mem " + str(i) + " =" + self.arr[int(i)])
