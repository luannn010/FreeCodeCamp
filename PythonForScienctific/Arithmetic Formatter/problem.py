from operate import Operator
from transform import Transform

class Problem:
    def __init__(self, problemL, bool=False):
        self.problemL = problemL
        self.bool = bool
        self.transformed_problems = self.transform()

    def __str__(self):
        if not len(self.problemL) <= 5:
            return "Error: Too many problems."
        if self.bool:
            result = []
            for problem in self.problemL:
                operator = Operator(problem)
                res = operator.calculate()
                result.append(f"{problem} = {res}")
            transformed_problems_str = self.transformed_problems if self.bool else ""
            return f"{transformed_problems_str}\n" + '\n'.join(result)
        else:
            return self.transformed_problems if self.transformed_problems else " "

    def transform(self):
        transformed_problems = []
        for problem in self.problemL:
            transformer = Transform(problem)
            transformed = transformer.transform()
            if transformed:
                transformed_problems.append(transformed)
        return '\n'.join(transformed_problems)


problem1 = Problem(["1 + 2", "2 + 7", "3 - 10", "4 + 7"], bool=True)
problem2 = Problem(["1 + 3", "2 - 9", "3 + 7", "4 + 2"])

print(problem1)
print(problem2)
