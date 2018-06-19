class ALU:

    def __init__(self, input1, input2, instruction):
        self.input1 = input1
        self.input2 = input2
        self.op = instruction
        self.zeroout = 0

    def run(self):
        if str(self.op) == "0000":  # add
            return bin(int(str(self.input1), 2) + int(str(self.input2), 2))[2:]
        elif str(self.op) == "0001":  # sub
            return bin(abs(int(str(self.input1), 2) - int(str(self.input2), 2)))[2:]
        elif str(self.op) == "0010":  # slt
            if int(str(self.input1)) < int(str(self.input2)):
                return 1
            else:
                return 0
        elif str(self.op) == "0011":  # or
            return bin(int(str(self.input1), 2) | int(str(self.input2), 2))[2:]
        elif str(self.op) == "0100":  # nand
            return bin(not (int(str(self.input1), 2) & int(str(self.input2), 2)))[2:]
        elif str(self.op) == "0101":  # addi
            return bin(int(str(self.input1), 2) + int(str(self.input2), 2))[2:]
        elif str(self.op) == "0110":  # slti
            if int(str(self.input1)) < int(str(self.input2)):
                return 1
            else:
                return 0
        elif str(self.op) == "0111":  # ori
            return bin(int(str(self.input1), 2) | int(str(self.input2), 2))[2:]
        elif str(self.op) == "1000":  # lui
            return bin(int(self.input2) << 16)[2:]
        elif str(self.op) == "1001":  # lw
            return bin(int(str(self.input1), 2) + int(str(self.input2), 2))[2:]
        elif str(self.op) == "1010":  # sw
            return bin(int(str(self.input1), 2) + int(str(self.input2), 2))[2:]
        elif str(self.op) == "1011":  # beq
            if (self.input2 == self.input1):
                self.zeroout = 1
                return 1
            else:
                return 0
        elif str(self.op) == "1100":  # jalr
            print("jalr")
        elif str(self.op) == "1101":  # J
            print("J")
