from graphics import *
win = GraphWin("pokeball display", 1000, 1650)
class pokeball(object):
    def __init__(self, x, y, topColor, bottomColor, cirColor, ):
        self.x = x
        self.y = y
        self.topColor = topColor
        self.bottomColor = bottomColor
        self.cirColor = cirColor

    def drawTop(self):
        top = Arc(Point(self.x, self.y), Point(self.x + 175, self.y - 152), 0, 180, "CHORD")
        top.setWidth(3)
        top.draw(win)
        top.setFill(self.topColor)

    def drawBottom(self):
        bottom = Arc(Point(self.x, self.y), Point(self.x + 175, self.y -152), 0, -180, "CHORD")
        bottom.setWidth(3)
        bottom.draw(win)
        bottom.setFill(self.bottomColor)

    def drawCircle(self):
        circle = Circle(Point(self.x + 85, self.y - 76), 25)
        circle.draw(win)
        circle.setFill(self.cirColor)






