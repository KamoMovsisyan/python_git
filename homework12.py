#1
class Triangle:
    count_ = 0

    def __new__(cls, *args, **kwargs):
        cls.count_ += 1
        return super().__new__(cls)

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self, height):
        return self.side1 * height / 2

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            raise ValueError('not same object')

        return (self.side1 == other.side1 and self.side2 == other.side2 and self.side3 == other.side3) or\
                (self.side1 == other.side2 and self.side2 == other.side1 and self.side3 == other.side3) or\
                (self.side1 == other.side2 and self.side2 == other.side3 and self.side3 == other.side1) or\
                (self.side1 == other.side3 and self.side2 == other.side1 and self.side3 == other.side2) or\
                (self.side1 == other.side1 and self.side2 == other.side3 and self.side3 == other.side2) or\
                (self.side1 == other.side3 and self.side2 == other.side2 and self.side3 == other.side2) 

    def is_alike(self, other):
        return Triangle.__eq__(self, other)

print(Triangle(1, 2, 3) == Triangle(3, 1, 2))

tri1 = Triangle(1, 2, 3)
tri2 = Triangle(3, 1, 2)

print(tri1.is_alike(tri2))

print(Triangle.count_)


#2
class Cube:
    def __init__(self, side):
        self.side = side
    
    def __eq__(self, other):
        return self.side == other.side

    def __gt__(self, other):
        return self.side > other.side

cube_1 = Cube(5)
cube_2 = Cube(3)
cube_3 = Cube(5)

print(cube_1 > cube_2)
print(cube_1 == cube_2)
print(cube_1 == cube_3)