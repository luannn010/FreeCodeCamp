from operate import Operator

class arithmetic_arranger(Operator):
    def __init__(self, problems, bool=False):
        super().__init__(problems)
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.line4 = []  # Result (default)
        self.bool = bool
        self.separate_lines()  # Automatically call separate_lines() during initialization
        self.get_dashes()
    def __str__(self):
        
        for i in range(len(self.problems)):
            line1 = "    ".join(str(item).rjust(4) for item in self.line1)
            line2 = "    ".join(str(item).rjust(4) for item in self.line2)
            line3 = "    ".join(str(item).rjust(4) for item in self.line3)
            if self.bool:
                line4 = "    ".join(str(item).rjust(4) for item in self.line4)
            line4 =""
        return f" {line1}\n{line2}\n{line3}\n{line4}"
    def get_dashes(self):
        for i in range(len(self.problems)):
            
            max_length_i = max(len(str(item)) for item in [self.line1[i], self.line2[i]])
            dashes = '-'*max_length_i
            self.line3.append(dashes)

    def separate_lines(self):
        for problem in self.problems:
            x, op, y = problem.split()
            k = op + " " + y
            self.line1.append(x)
            self.line2.append(k)
            self.line4 = self.calculate()
