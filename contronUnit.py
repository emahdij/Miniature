class controlUnit:
    RegDst = 0
    Branch = 0
    MemRead = 0
    MemtoReg = 0
    ALUop = 0
    MemWrite = 0
    ALUsrc = 0
    Regwrite = 0
    Junp = 0

    muxalu = 0
    muxregister = 0
    muxwb = 0
    muxjump = 0

    def __init__(self, instinput):
        self.instrution = instinput
        self.ALUop = instinput
        self.controfill()
        self.muxfill()

    def controfill(self):
        a = self.instrution
        if a == "0000" or a == "0001" or a == "0010" or a == "0011" or a == "0100":  # Rtype
            self.RegDst = 1
            self.ALUsrc = 0
            self.MemtoReg = 0
            self.Regwrite = 1
            self.MemRead = 0
            self.MemWrite = 0
            self.Branch = 0
            self.Junp = 0
        elif a == "1001":  # lw
            self.RegDst = 0
            self.ALUsrc = 1
            self.MemtoReg = 1
            self.Regwrite = 1
            self.MemRead = 1
            self.MemWrite = 0
            self.Branch = 0
            self.Junp = 0
        elif a == "1010":  # sw
            self.ALUsrc = 1
            self.Regwrite = 0
            self.MemRead = 0
            self.MemWrite = 1
            self.Branch = 0
            self.Junp = 0
        elif a == "1011":  # beq
            self.ALUsrc = 0
            self.Regwrite = 0
            self.MemRead = 0
            self.MemWrite = 0
            self.Branch = 1
            self.Junp = 0
        elif a == "1101":  # jump
            self.RegDst = 0
            self.ALUsrc = 0
            self.MemtoReg = 0
            self.Regwrite = 0
            self.MemRead = 0
            self.MemWrite = 0
            self.Branch = 0
            self.Junp = 1
        elif a == "0101" or a == "0111" or a == "1000":  # addi ,slti,ori,lui
            self.RegDst = 0
            self.ALUsrc = 1
            self.MemtoReg = 0
            self.Regwrite = 1
            self.MemRead = 0
            self.MemWrite = 0
            self.Branch = 0
            self.Junp = 0
        elif a == "0110":
            self.RegDst = 0
            self.ALUsrc = 0
            self.MemtoReg = 0
            self.Regwrite = 1
            self.MemRead = 0
            self.MemWrite = 0
            self.Branch = 0
            self.Junp = 0

    def muxfill(self):
        self.muxregister = self.RegDst
        self.muxalu = self.ALUsrc
        self.muxwb = self.MemtoReg
        self.muxjump = self.Junp
