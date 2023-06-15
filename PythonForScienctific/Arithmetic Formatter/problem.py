from dataclasses import dataclass, field

@dataclass
class Problem:
    problemL: list
    arguments: bool = field(default=False)

    def __init__(self, problemL, arguments=False):
        if len(problemL) <= 4:
            self.problemL = problemL
        else:
            raise ValueError("Error: Too many problems.")
        self.arguments = arguments

problem1 = Problem(["1", "2", "3", "4", "5"], True)  # Raises ValueError
problem2 = Problem(["1", "2", "3", "4"], True)       # No error

print(problem1)
print(problem2)
