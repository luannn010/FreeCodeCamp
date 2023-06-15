


class Problem:
    
    def __init__(self, problemL, args = None):
        super().__init__()
        self.problemL = problemL
        self.args = args
   
    # def __str__(self): # Format 
    #     return
    
    def __setattr__(self,name, value):
        if (name == "problemL"):
            if len(value) <=4:
                return "Nice"
        return "Error: Too many problems."



problem1 = Problem(["1", "2", "3", "4", "5"])
problem2 = Problem(["1", "2", "3", "4"])

print(problem1)
print(problem2)
