class Line:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def length(self)->int:
        return self.y - self.x
    
    def __cmp__(self, other:"Line"):
        if self.length() > other.length():
            return "Лінія  1 довша"
        elif self.length() < other.length():
            return "Лінія  2 довша"
        else:
            return "Лінії однакові"


line_1 = Line(1, 5)
line_2 = Line(4, 7)

print(line_1.length())
print(line_2.length())
print(line_1.__cmp__(line_2))

