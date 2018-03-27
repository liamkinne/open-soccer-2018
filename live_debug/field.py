class Field(object):
    def __init__(self, x, y, w=200):
        self.x = x
        self.y = y
        self.ratio = 2430.0 / 1820.0
        self.w = w
        self.h = self.w * self.ratio
        self.px_mm = self.w/1820.0
        self.side = 'yellow'
    
    def rect(self, x, y, w, h):
        x = self.x + (x * self.px_mm)
        y = self.y + (y * self.px_mm)
        w = (w * self.px_mm)
        h = (h * self.px_mm)
        rect(x, y, w, h)
    
    def display(self):
        # background
        stroke(0)
        strokeWeight(2)
        fill(0, 180, 0)
        self.rect(0, 0, 1820, 2430)
        # white boundary line
        stroke(0)
        strokeWeight(0)
        fill(255, 255, 255)
        self.rect(250, 250, 1820-500, 2430-500)
        fill(0, 180, 0)
        self.rect(300, 300, 1820-600, 2430-600)
        # goal boundaries
        fill(0, 0, 0)
        self.rect(1820/2 - 450, 300, 900, 300)
        self.rect(1820/2 - 450, 2430-600, 900, 300)
        fill(0, 180, 0)
        self.rect(1820/2 - 425, 300, 850, 275)
        self.rect(1820/2 - 425, 2430-575, 850, 275)
        # goals
        if self.side == 'cyan':
            fill(0, 255, 255)
        else:
            fill(255, 255, 64)
        self.rect(1820/2 - 225, 226, 450, 74)
        if self.side == 'yellow':
            fill(0, 255, 255)
        else:
            fill(255, 255, 64)
        self.rect(1820/2 - 225, 2430-300, 450, 75)
        fill(0, 0, 0)
        self.rect(1820/2 - 25, 2430/2 - 25, 50, 50)
