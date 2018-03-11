from pokeball import *

class Moonball(Pokeball):


    def __init__(self, x, y, topColor, bottomColor, cirColor, moonColor):
        super(Moonball, self).__init__(x, y, topColor, bottomColor, cirColor)
        self.moonColor = moonColor

    def drawMoon(self):
        moon = Circle(Point(self.x + 85, self.y - 120), 25)
        crescent = Circle(Point(self.x + 99, self.y - 114), 25)
        moon.draw(win)
        moon.setFill(self.moonColor)
        crescent.draw(win)
        crescent.setOutline(self.topColor)
        crescent.setFill(self.topColor)
        win.getMouse()



