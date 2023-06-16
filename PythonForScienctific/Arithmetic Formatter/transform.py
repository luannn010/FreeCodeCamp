from operate import Operator


class Transform:
    def __init__(self, problem):
        self.problem = problem
        self.result = None

    def add_newline(self):
        operators = ['+', '-']
        for operator in operators:
            self.problem = self.problem.replace(' '+operator,'\n' + operator + ' ')

    def calculate(self):
        operator = Operator(self.problem)
        self.result = operator.calculate()

    def transform(self):
        self.add_newline()
        
        lines = self.problem.split('\n')

        # Calculate the maximum line length
        max_length = max(len(line) for line in lines)

        # Create a line of dashes with the same length
        dashes = '-' * max_length

        # Right-align each line using string formatting
        aligned_lines = [line.rjust(max_length) for line in lines]
        aligned_result = [str(self.result).rjust(max_length)]

        # Join the aligned lines and dashes into a string
        aligned_string = '\n'.join(aligned_lines + [dashes] + aligned_result)
        return aligned_string
    


