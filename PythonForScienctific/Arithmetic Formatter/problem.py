from operate import Operator
from dataclasses import dataclass, field

@dataclass
class Problem(Operator):
    problemL : list
    arguments: bool = field(default=False)

    def has_less_then_4(self):
        if  len(self.problemL) <= 4:
            for item in self.problemL:
                print(item)
        else:
            return "Error: Too many problems."

    

