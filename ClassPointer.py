from math import sqrt

class Point:
     def __init__(self, initialX = 0, initialY = 0):
          self.x = initialX
          self.y = initialY
     
     def move(self,dx,dy):
          self.x += dx
          self.y += dy
          
     def getX(self):
          return self.x
     def getY(self):
          return self.y
     
     def distance(self,other):
          dx = self.x - other.x
          dy = self.y - other.y
          return sqrt(dx*dx + dy*dy)