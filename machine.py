from ALU import ALU
from DataMem import DataMem
from Registerfiles import registers
from contronUnit import controlUnit


class Minature:
    bininput = ""

    def __init__(self, inputtxt):
        self.inputtxt = inputtxt
        self.register = registers()
        self.memory = DataMem()

    def run(self):
        # print(self.inputtxt)
        pc = 0
        while pc < len(self.inputtxt):
            # print(self.inputtxt[i])
            print("Pc: " + str(pc))
            control = controlUnit(self.inputtxt[pc][4:8])
            rs = self.inputtxt[pc][8:12]
            rt = self.inputtxt[pc][12:16]
            if control.muxregister == 1:
                rd = self.inputtxt[pc][16:20]
            elif control.muxregister == 0:
                rd = self.inputtxt[pc][12:16]
            inputalu1 = self.register.getregister(int(rs, 2))
            writememdata = self.register.getregister(int(rt, 2))
            if (control.muxalu == 0):
                inputalu2 = self.register.getregister(int(rt, 2))
            else:
                inputalu2 = self.inputtxt[pc][16] * 16 + self.inputtxt[pc][16:]

            # print(inputalu1, "  ", inputalu2)
            alu = ALU(inputalu1, inputalu2, self.inputtxt[pc][4:8])
            aluresult = alu.run()

            if control.Branch == 1 and aluresult == 1:
                pc = int(str(self.inputtxt[pc][16:]), 2) - 1

            if control.MemRead == 1 and control.MemWrite == 0:
                memresult = self.memory.get(aluresult)
            elif control.MemRead == 0 and control.MemWrite == 1:
                self.memory.set(int(str(aluresult), 2), writememdata)
            if control.muxwb == 0 and control.Regwrite == 1:
                self.register.setregister(int(str(rd), 2), aluresult)
            elif control.muxwb == 1 and control.Regwrite == 1:
                self.register.setregister(int(str(rd), 2), str(memresult))

            print(self.register.register)
            self.memory.printMem()
            print("--------------------")
            pc += 1
