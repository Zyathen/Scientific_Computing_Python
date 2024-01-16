#Creating a program to determine the area of polygons

class Rectangle:
    # Initialize a rectange
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    # Sets the width
    def set_width(self, width):
        self.width = width

    # Sets the height
    def set_height(self, height): 
        self.height = height

    # Calculates the area
    def get_area(self):
        return self.height * self.width
    
    # Calculates the perimeter
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    # Calculates the diagonal
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    # Returns string of the shape
    def get_picture(self):
        # If the width or height is too big
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ""

        for i in range(0, self.height):
            picture += ("*" * self.width) + "\n"
        
        return picture

    #Takes another shape, return number of times shape could fit inside of the shape (no rotations)
    def get_amount_inside(self, shape):
        if self.get_area() < shape.get_area() or self.width < shape.width or self.height < shape.height:
            return 0
        
        num_across = self.width // shape.width
        num_down = self.height // shape.height

        return num_across * num_down


# subclass for rectangle
class Square(Rectangle):
    # Initializing with a side length
    def __init__(self, side):
        super().__init__(side, side)

    def set_height(self, height):
       self.height = height
       self.width = height
    
    def set_width(self, width):
        self.height = width
        self.width = width

    def __str__(self):
        return "Square(side={})".format(self.height)

    def set_side(self, side):
        self.height = side
        self.width = side

    