class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self, new_width):
        self.width = new_width
        return self.width
    def set_height(self, new_height):
        self.height = new_height
        return self.height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return self.width*2 + self.height*2
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        shape = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                shape += self.width * "*" + "\n"
            return shape
    def get_amount_inside(self, shape):
        new_width = shape.width
        new_height = shape.height
        times = (self.width // new_width)*(self.height // new_height)
        return times




class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(width=side, height=side)

    def set_side(self, new_side):
        self.side = new_side
        self.width = new_side
        self.height = new_side
        self.diagonal = (2 * new_side ** 2) ** 0.5
    def set_width(self, new_side):
        self.side = new_side


    def __str__(self):
        return f"Square(side={self.side})"

