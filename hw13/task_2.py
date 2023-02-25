import math

def distance(x1, y1, x2, y2):
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Rectangle:
  def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x2, y2, x3, y3)
    d3 = distance(x3, y3, x4, y4)
    d4 = distance(x4, y4, x1, y1)
    if d1 != d3 or d2 != d4:
      print("Неправильно введені вершини")
      return
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    self.x3 = x3
    self.y3 = y3
    self.x4 = x4
    self.y4 = y4
    
  def perimeter(self):
    return 2 * (distance(self.x1, self.y1, self.x2, self.y2) + distance(self.x2, self.y2, self.x3, self.y3))
    
  def area(self):
    return distance(self.x1, self.y1, self.x2, self.y2) * distance(self.x2, self.y2, self.x3, self.y3)


class Circle:
  def __init__(self, x, y, r):
    self.x = x
    self.y = y
    self.r = r
    
  def perimeter(self):
    return 2 * math.pi * self.r
    
  def area(self):
    return math.pi * self.r**2

class Triangle:
  def __init__(self, x1, y1, x2, y2, x3, y3):    
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x2, y2, x3, y3)
    d3 = distance(x3, y3, x1, y1)
    if d1 + d2 <= d3 or d2 + d3 <= d1 or d3 + d1 <= d2:
      print("Неправильно введені вершини")
      return
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    self.x3 = x3
    self.y3 = y3

  def perimeter(self):
    return distance(self.x1, self.y1, self.x2, self.y2) + distance(self.x2, self.y2, self.x3, self.y3) + distance(self.x3, self.y3, self.x1, self.y1)

  def area(self):
    a = distance(self.x1, self.y1, self.x2, self.y2)
    b = distance(self.x2, self.y2, self.x3, self.y3)
    c = distance(self.x3, self.y3, self.x1, self.y1)
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))



rect = Rectangle(0, 0, 0, 1, 1, 1, 1, 0)
print("Прямокутник")
print("Периметр:", rect.perimeter())
print("Площа:", rect.area())

circle = Circle(0, 0, 1)
print("Коло")
print("Периметр:", circle.perimeter())
print("Площа:", circle.area())

tri = Triangle(0, 0, 1, 1, 2, 0)
print("Трикутник")
print("Периметр:", tri.perimeter())
print("Площа:", tri.area())

