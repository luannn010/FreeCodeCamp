def arithmetic_arranger(problems, bool=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    operator = ['+', '-']

    for problem in problems:
        x, op, y = problem.split()

        if op not in operator:
            return "Error: Operator must be '+' or '-'."

        if not x.isdigit() or not y.isdigit():
            return "Error: Numbers must only contain digits."

        if len(x) > 4 or len(y) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_length = max(len(x), len(y)) + 2
        line1.append(x.rjust(max_length))
        line2.append(op + y.rjust(max_length - 1))
        line3.append('-' * max_length)

        if bool:
            if op == '+':
                result = str(int(x) + int(y))
            else:
                result = str(int(x) - int(y))
            line4.append(result.rjust(max_length))

    arranged_problems = []
    arranged_problems.append('    '.join(line1))
    arranged_problems.append('    '.join(line2))
    arranged_problems.append('    '.join(line3))

    if bool:
        arranged_problems.append('    '.join(line4))

    return '\n'.join(arranged_problems)
