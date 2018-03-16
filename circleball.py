from pokeball import *

class CircleBall(Pokeball):
    def __init__(self, x, y, topColor, bottomColor, cirColor, designColor):
        super(CircleBall, self).__init__(x, y, topColor, bottomColor, cirColor)
        self.designColor = designColor

    def drawDesign(self):
        c1 = Circle(Point(self.x + 85, self.y - 85), 40)
        c2 = Circle(Point(self.x + 85, self.y - 118), 35)
        c3 = Circle(Point(self.x + 135, self.y - 76), 35)
        c4 = Circle(Point(self.x + 40, self.y - 76), 35)
        c1.draw(win)
        c2.draw(win)
        c3.draw(win)
        c4.draw(win)
        c1.setFill(self.designColor)
        c1.setOutline(self.designColor)
        c2.setFill(self.designColor)
        c2.setOutline(self.designColor)
        c3.setFill(self.designColor)
        c3.setOutline(self.designColor)
        c4.setFill(self.designColor)
        c4.setOutline(self.designColor)
        l = Line(Point(self.x, self. y - 76),Point(self.x + 175 , self.y - 76))
        l.setWidth(3)
        l.draw(win)

