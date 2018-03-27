from field import *
from robot import *

def setup():
    size(640, 480)
    
field = Field(10, 10, w=640/2)
robot = Robot(field, 1820/2, 2430/2 + 400)

def draw():
    global field, robot
    background(200)
    field.display()
    robot.display()
    
