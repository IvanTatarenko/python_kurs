from typing import Type

class Vector:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __add__(self, other: Type['Vector']) -> Type['Vector']:
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Type['Vector']) -> Type['Vector']:
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: int) -> Type['Vector']: 
        return Vector(self.x * scalar, self.y * scalar)
    
    def __matmul__(self, other: Type['Vector']) -> int:
        return self.x * other.x + self.y * other.y

    
v1 = Vector(3,4)
v2 = Vector(2,3)

assert (v1 + v2).x == 5 and (v1 + v2).y == 7
assert (v1 - v2).x == 1 and (v1 - v2).y == 1
assert (v1 * 3).x == 9 and (v1 * 3).y == 12
assert (v1 @ v2) == 18
  