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
        fill(0, 0, 128)
        x = self.field.x + self.x
        y = self.field.y + self.y
        ellipse(x, y, self.radius * 2, self.radius * 2)
        angle = self.angle * (3.14/180.0)
        stroke(32, 255, 32)
        strokeWeight(0.5)
        view_angle = 140
        for a in [-view_angle/2.0, view_angle/2.0]:
            a *= (3.14/180)
            line(x - (sin(-angle) * (self.radius - 5)), y - (cos(-angle) * (self.radius - 5)), x - (sin(-angle + a) * 250), y - (cos(-angle + a) * 250))
    
