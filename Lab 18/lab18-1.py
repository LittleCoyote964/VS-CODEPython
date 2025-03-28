class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __add__(self, other):
        return rectangle(self.width + other.width, self.height + other.height)
    def area(self):
        return self.width * self.height

rec1 = rectangle(3, 4)
rec2 = rectangle(7, 4)
rec3 = rec1 + rec2

print("New rectangle:", rec3.width, rec3.height)
print("New rectangle area:", rec3.area())