from pokeball import *

class Rball(object):








def R(win):
    r = Text(Point(825, 500), "R")
    r.draw(win)


def main():
    Rball(win)
    win.getMouse()
    win.close()





main()





