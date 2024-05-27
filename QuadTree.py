class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)
    
    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        if scalar == 0:
            return None
        return Vector(self.x / scalar, self.y / scalar)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, vector):
        return self.x == vector.x and self.y == vector.y
    

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 0, 0)
        self.radius = 10
        self.Vector = Vector(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, Point):
        return Point.x == self.x and Point.y == self.y and Point.Vector == self.Vector
    
    def distance(self, Point):
        return ((self.x - Point.x) ** 2 + (self.y - Point.y) ** 2) ** 0.5


class QuadTree:
    def __init__(self, TopLeftPoint, BottomRightPoint):
        self.TopLeftPoint = TopLeftPoint
        self.BottomRightPoint = BottomRightPoint
        self.Capacity = 4
        self.devided = False
        self.TopLeftTree = None
        self.TopRightTree = None
        self.BottomLeftTree = None
        self.BottomRightTree = None
        self.listPoints = []

    def inBoundary(self, Point):
        return (
            self.TopLeftPoint.x <= Point.x
            and self.TopLeftPoint.y <= Point.y
            and self.BottomRightPoint.x > Point.x
            and self.BottomRightPoint.y > Point.y
        )

    def devide(self):
        self.TopLeftTree = QuadTree(
            self.TopLeftPoint,
            Point(
                (self.BottomRightPoint.x + self.TopLeftPoint.x) / 2,
                (self.BottomRightPoint.y + self.TopLeftPoint.y) / 2,
            ),
        )

        self.TopRightTree = QuadTree(
            Point(
                (self.BottomRightPoint.x + self.TopLeftPoint.x) / 2, self.TopLeftPoint.y
            ),
            Point(
                self.BottomRightPoint.x,
                (self.BottomRightPoint.y + self.TopLeftPoint.y) / 2,
            ),
        )

        self.BottomLeftTree = QuadTree(
            Point(
                self.TopLeftPoint.x, (self.BottomRightPoint.y + self.TopLeftPoint.y) / 2
            ),
            Point(
                (self.BottomRightPoint.x + self.TopLeftPoint.x) / 2,
                self.BottomRightPoint.y,
            ),
        )
        self.BottomRightTree = QuadTree(
            Point(
                (self.BottomRightPoint.x + self.TopLeftPoint.x) / 2,
                (self.BottomRightPoint.y + self.TopLeftPoint.y) / 2,
            ),
            self.BottomRightPoint,
        )
        self.devided = True

    def insert(self, Point):
        if not self.inBoundary(Point):
            return False

        if len(self.listPoints) < self.Capacity:
            self.listPoints.append(Point)
            return True

        if self.devided == False:
            self.devide()

        if self.TopLeftTree.inBoundary(Point):
            self.TopLeftTree.insert(Point)
            return True

        if self.TopRightTree.inBoundary(Point):
            self.TopRightTree.insert(Point)
            return True

        if self.BottomLeftTree.inBoundary(Point):
            self.BottomLeftTree.insert(Point)
            return True

        if self.BottomRightTree.inBoundary(Point):
            self.BottomRightTree.insert(Point)
            return True

    def search(self, Point):
        for p in self.listPoints:
            if p == Point:
                print("Found!")
                return True

        if self.devided == True:
            if self.TopLeftTree.inBoundary(Point):    
                print("TopLeft")
                self.TopLeftTree.search(Point)
                return

            if self.TopRightTree.inBoundary(Point):    
                print("TopRight")
                self.TopRightTree.search(Point)
                return

            if self.BottomLeftTree.inBoundary(Point):    
                print("BottomLeft")
                self.BottomLeftTree.search(Point)
                return

            if self.BottomRightTree.inBoundary(Point):    
                print("BottomRight")
                self.BottomRightTree.search(Point)
                return

        print("Not found!")
        return False
    
    def search(self, TopLeft, BottomRight):
        listPoints = []
        if self.check_intersection(TopLeft, BottomRight) == False:
            return

        for p in self.listPoints:
            if p.x >= TopLeft.x and p.x <= BottomRight.x and p.y >= TopLeft.y and p.y <= BottomRight.y:
                listPoints.append(p)

        if self.devided == True:

            result = self.TopLeftTree.search(TopLeft, BottomRight)
            if result != None:
                listPoints += result

            result = self.TopRightTree.search(TopLeft, BottomRight)
            if result != None:
                listPoints += result

            result = self.BottomLeftTree.search(TopLeft, BottomRight)
            if result != None:
                listPoints += result
            
            result = self.BottomRightTree.search(TopLeft, BottomRight)
            if result != None:
                listPoints += result

        return listPoints
        

    def depth(self):
        if self.devided == False:
            return 0

        return (
            max(
                self.TopLeftTree.depth(),
                self.TopRightTree.depth(),
                self.BottomLeftTree.depth(),
                self.BottomRightTree.depth(),
            )
            + 1
        )

    def __str__(self):
        str = ""
        for p in self.listPoints:
            print(p)

        return str

    def print(self):
        for p in self.listPoints:
            print(p)

        if self.devided == True:
            self.TopLeftTree.print()

            self.TopRightTree.print()

            self.BottomLeftTree.print()

            self.BottomRightTree.print()

    def check_intersection(self, TopLeft, BottomRight):
        if self.TopLeftPoint.x > BottomRight.x or self.BottomRightPoint.x < TopLeft.x:
            return False

        if self.TopLeftPoint.y > BottomRight.y or self.BottomRightPoint.y < TopLeft.y:
            return False

        return True

    
