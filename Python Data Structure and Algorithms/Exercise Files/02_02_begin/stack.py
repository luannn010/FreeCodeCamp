"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    def __init__(self):
        self.items = []
    
    # check if empty
    def is_empty(self):
        return not self.items
    
    # push item to list
    def push(self, item):
        self.items.append(item)

    # remove last item in list
    def pop(self):
        return self.items.pop()
    
    # return last item in list
    def peek(self):
        return self.items[-1]
    
    # return size of list
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)



