
class Coordinate:

    def __init__(self, x=None, y=None):
        if x is None:
            self.x = 0
        else:
            self.x = x

        if y is None:
            self.y = 0
        else:
            self.y = y

    def incremental(self, x, y):
        self.x += x
        self.y += y
