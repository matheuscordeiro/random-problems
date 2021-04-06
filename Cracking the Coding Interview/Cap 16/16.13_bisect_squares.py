class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, A: Point, B: Point):
        self.A = A
        self.B = B

    @property
    def slopes(self):
        return (self.B.y - self.A.y) / (self.B.x - self.A.x)

    @property
    def y_intercept(self):
        return self.A.y - self.A.x * self.slopes

    def is_same_to(self, L):
        return self.slopes == L.slopes and self.y_intercept == L.y_intercept


class Squares:
    def __init__(self, A: Point, B: Point, C: Point, D: Point):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def get_horizontal_line(self):
        y = (self.B.y - self.A.y)/2 + self.A.y
        first = Point(self.A.x, y)
        last = Point(self.D.x, y)
        return Line(first, last)

    def get_vertical_line(self):
        x = (self.D.x - self.A.x)/2 + self.A.x
        first = Point(x, self.A.y)
        last = Point(x, self.B.y)
        return Line(first, last)

    def get_diagonal_to_right(self):
        return Line(self.A, self.C)

    def get_diagonal_to_left(self):
        return Line(self.D, self.B)


if __name__ == "__main__":
    A = Point(2,1)
    B = Point(2,4)
    C = Point(5,4)
    D = Point(5,1)
    s1 = Squares(A, B, C, D)

    A2 = Point(3,2)
    B2 = Point(3,3)
    C2 = Point(4,3)
    D2 = Point(4,2)
    s2 = Squares(A2, B2, C2, D2)
    print(s1.get_diagonal_to_right().is_same_to(s2.get_diagonal_to_right()))