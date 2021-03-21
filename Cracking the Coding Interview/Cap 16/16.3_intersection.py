class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'


class Line:

    def __init__(self, A: Point, B: Point):
        self.A = A
        self.B = B

    @property
    def slopes(self):
        rise = self.B.y - self.A.y
        run = self.B.x - self.A.x
        return (rise)/(run)  # ZeroDivisionError (slopes should be infinity)

    @property
    def y_intersept(self):
        return self.B.y - (self.slopes * self.B.x)

    def get_y(self, x):
        return x * self.slopes + self.y_intersept


def point_intersection(A: Point, B: Point, C: Point, D: Point):

    # create lines
    first_line = Line(A, B)
    second_line = Line(C, D)

    # the lines are parallel
    if first_line.slopes == second_line.slopes:
        if first_line.y_intersept == second_line.y_intersept: 
            if is_between(first_line.A, second_line.A, first_line.B):
                return second_line.A
            if is_between(first_line.A, second_line.B, first_line.B):
                return second_line.B
        return None

    # point of intersection
    x = (second_line.y_intersept - first_line.y_intersept)/(first_line.slopes - second_line.slopes)
    y = first_line.get_y(x)
    point = Point(x, y)
    if is_between_points(first_line.A, point, first_line.B) and is_between_points(second_line.A, point, second_line.B):
        return point

    return None

def is_between(start, middle, end) -> bool:
    return start <= middle <= end


def is_between_points(start: Point, middle: Point, end: Point) -> bool:
    return is_between(start.x, middle.x, end.x) and is_between(start.y, middle.y, end.y)


if __name__ == '__main__':
    A = Point(15, 10)
    B = Point(49, 25)
    C = Point(29, 5)
    D = Point(32, 32)
    print(point_intersection(A, B, C, D))
