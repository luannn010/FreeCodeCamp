from operate import Operator

string1 = Operator("123 + 456")
result = string1.calculate()

def add_newline(problem):
    operators = ['+', '-']
    for operator in operators:
        problem = problem.replace(operator, '\n' + operator + '  ')
    return problem

string = add_newline(string1.problem)


def transform(lines, result):
    # Calculate the maximum line length
    max_length = max(len(line) for line in lines)

    # Create a line of dashes with the same length
    dashes = '-' * max_length

    # Right-align each line using string formatting
    aligned_lines = [line.rjust(max_length) for line in lines]
    aligned_result = [str(result).rjust(max_length)]
    # Join the aligned lines and dashes into a string
    aligned_string = '\n'.join(aligned_lines + [dashes] + aligned_result)
    return aligned_string

lines = string.split('\n')
print(transform(lines, result))
