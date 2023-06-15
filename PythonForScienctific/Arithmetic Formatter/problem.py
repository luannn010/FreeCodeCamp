from operate import Operator

class arithmetic_arranger(Operator):
    def __init__(self, problemL, bool=False):
        super().__init__()
        self.problemL = problemL
        self.bool = bool
   
    def __str__(self):
        if not len(self.problemL) <= 4:
            return "Error: Too many problems."
        if self.bool:
            result = []
            for problem in self.problemL:
                res = self.calculate(problem)
                result.append(f"{problem} = {res}")
            return '\n'.join(result)
        else:
            return '\n'.join(self.problemL)


problem1 = arithmetic_arranger(["1 + 2", "2 + 7", "3 - 10", "4 + 7"], True)
problem2 = arithmetic_arranger(["1 + 3", "2 - 9", "3 + 7", "4 + 2"])

print(problem1)
print(problem2)
print(problem1.bool)
print(problem2.bool)
