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

    def __str__(self):
        
        max_lengths = [max(len(line) for line in self.line1 + self.line2 + self.line3)]
        for max_length in max_lengths:
            dashes = '-' * max_length
            self.line3.append(dashes)

        
        line1 = "    ".join(str(item).rjust(max_length) for item in self.line1)
        line2 = "    ".join(str(item).rjust(max_length) for item in self.line2)
        line3 = "    ".join(str(item) for item in self.line3)
        line4 = "    ".join(str(item).rjust(max_length) for item in self.line4)
        
        return f"{line1}\n{line2}\n{line3}\n{line4}"

    def separate_lines(self):
        for problem in self.problems:
            x, op, y = problem.split()
            k = op + " " + y
            self.line1.append(x)
            self.line2.append(k)
            if self.bool:
                self.line4 = self.calculate()
            else:
                self.line4 = []
