class rajuturaikata():
    def rajut(self,kata):
        self.kata = kata
        rajut1 = ""
        for i in range(len(self.kata)):
            for j in range(i):
                rajut1 +=1
            if i+1 <= len(self.kata):
                rajut1 += self.kata[i+1]
        return rajut1
    def urai(self,kata):
        self.kata = kata
        urai1 = ""
        for i in range(len(self.kata)):
            for j in range(i+1):
                urai1 += self.kata[j]
        return urai1
x = rajuturaikata()
print(x.urai("python"))
print(x.rajut("CCoCodCode"))





