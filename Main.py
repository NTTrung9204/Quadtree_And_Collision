import pygame, sys
from pygame.locals import *
from QuadTree import QuadTree, Point, Vector
import numpy as np

FRAME = 0
COLLISION = 0

listPoints = []
for _ in range(2000):
    # Color = (
    #     np.random.randint(0, 255),
    #     np.random.randint(0, 255),
    #     np.random.randint(0, 255),
    # )
    newPoint = Point(np.random.randint(0, 1200), np.random.randint(0, 700))
    newVector = Vector(np.random.randint(-10, 10), np.random.randint(-10, 10))
    newPoint.Vector = newVector
    newPoint.radius = 2
    newPoint.Color = (0, 255, 0)
    listPoints.append(newPoint)


listPoints[0].Color = (255, 0, 0)
# listPoints[0].radius = 5
# listPoints[0].Vector = Vector(3, 0)
# listPoints[0].x = 400
# listPoints[0].y = 400
# listPoints[1].x = 400
# listPoints[1].y = 400
# listPoints[1].radius = 5
# listPoints[1].Vector = Vector(-3, 0)



def drawPoints():
    for point in listPoints:
        pygame.draw.circle(DISPLAYSURF, point.Color, (int(point.x), int(point.y)), point.radius)


def updatePoints():
    for point in listPoints:
        point.x += point.Vector.x / 10
        point.y += point.Vector.y / 10
        if point.x < 0 or point.x > 1200:
            point.Vector.x *= -1
        if point.y < 0 or point.y > 700:
            point.Vector.y *= -1


def buildQuadTree():
    MyTree = QuadTree(Point(0, 0), Point(1200, 700))
    for point in listPoints:
        MyTree.insert(point)
    return MyTree

def CalculateVector(PointA, PointB):
    WeightA = PointA.radius ** 2
    WeightB = PointB.radius ** 2

    VectorA = ((WeightA - WeightB) * PointA.Vector + (2 * WeightB) * PointB.Vector) / (WeightA + WeightB)
    VectorB = ((WeightB - WeightA) * PointB.Vector + (2 * WeightA) * PointA.Vector) / (WeightA + WeightB)

    return VectorA, VectorB



def checkCollision(MyTree, COLLISION):
    radius = 2
    dictVectorAfterCollision = {}

    for i in range(len(listPoints)):
        listCollisions = MyTree.search(
            Point(listPoints[i].x - (2 * radius + 1), listPoints[i].y - (2 * radius + 1)),
            Point(listPoints[i].x + (2 * radius + 1), listPoints[i].y + (2 * radius + 1)),
        )
        if len(listCollisions) > 1:
            for point in listCollisions:
                if point != listPoints[i]:

                    if point.distance(listPoints[i]) <= point.radius + listPoints[i].radius:
                        overlap = point.radius + listPoints[i].radius - point.distance(listPoints[i])
                        listPoints[i].x -= overlap

                        dictVectorAfterCollision[i], _ = CalculateVector(listPoints[i], point)
                        if dictVectorAfterCollision[i] == _:
                            dictVectorAfterCollision[i] = Vector(-dictVectorAfterCollision[i].x, -dictVectorAfterCollision[i].y)
                        # print(dictVectorAfterCollision[i], _)
                        
                        if point.Color == (255, 0, 0):
                            listPoints[i].Color = (255, 0, 0)

                        COLLISION += 1
                        # pygame.display.set_caption(f"COLLISION: {COLLISION}")
                        #pause game in 10 seconds
                        # pygame.time.wait(10000)
    
    for index in dictVectorAfterCollision:
        listPoints[index].Vector = dictVectorAfterCollision[index]

    return COLLISION


pygame.init()

DISPLAYSURF = pygame.display.set_mode((1200, 700))
pygame.display.set_caption(f"COLLISION: {COLLISION}")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill((255, 255, 255))

    updatePoints()
    MyTree = buildQuadTree()
    COLLISION = checkCollision(MyTree, COLLISION)

    drawPoints()
    FRAME += 1
    pygame.display.update()
