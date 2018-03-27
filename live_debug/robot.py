class Robot(object):
    def __init__(self, field, x, y):
        self.field = field
        self.set_position( x, y)
        self.set_angle(0)
        self.radius = 110 * self.field.px_mm
    
    def set_position(self, x, y):
        self.x = x * self.field.px_mm
        self.y = y * self.field.px_mm
        
    def set_angle(self, angle):
        self.angle = angle
    
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(240)
        ellipse(self.field.x + self.x, self.field.y + self.y, self.radius * 2, self.radius * 2)
