import re
class Operator:
    def calculate(self, problem):
        problem = problem.replace(" ", "")
        match = re.search('([-+])', problem)
        if match:
            operator = match.group(1)
            x, y = re.split('[-+#]', problem)
            if not x.isdigit() or not y.isdigit():
                return "Error: Numbers must only contain digits."
            x = int(x)
            y = int(y)
            if not (-1000 < x < 1000) or not (-1000 < y < 1000):
                return "Error: Numbers cannot be more than four digits."
            if operator == "+":
                return x + y
            elif operator == "-":
                return x - y
        return "Error: Operator must be '+' or '-'."

