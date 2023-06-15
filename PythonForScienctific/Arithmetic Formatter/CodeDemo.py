string1 = "123+1332"
result = "1213"
def add_newline(string):
    operators = ['+', '-', ]
    for operator in operators:
        string = string.replace(operator, '\n' + operator + '  ')
    return string
string = add_newline(string1)
def transform(lines , result):
    # Split the string into lines
    lines = string.split('\n')

    # Calculate the maximum line length
    max_length = max(len(line) for line in lines)

    # Create a line of dashes with the same length
    dashes = '-' * max_length

    # Right-align each line using string formatting
    aligned_lines = [line.rjust(max_length) for line in lines]
    aligned_result = [result.rjust(max_length)]
    # Join the aligned lines and dashes into a string
    aligned_string = '\n'.join(aligned_lines + [dashes] + aligned_result)
    return aligned_string
print(transform(add_newline(string1),result))


