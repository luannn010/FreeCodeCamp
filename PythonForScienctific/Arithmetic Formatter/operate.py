class Operator:
    def __init__(self, problems):
        self.problems = problems

    def __str__(self):
        return str(self.problems)

    def calculate(self):
        operator = ['+', '-']
        result = []
        for problem in self.problems:
            x, op, y = problem.split()
            if op in operator:
                if x.isdigit() and y.isdigit():
                    x = int(x)
                    y = int(y)
                    if -10000 < x < 10000 and -10000 < y < 10000:
                        result.append(eval(problem))
                    else:
                        return "Error: Numbers cannot be more than five digits."
                else:
                    return "Error: Numbers must only contain digits."
            else:
                return "Error: Operator must be '+' or '-'."
        return result
