class BaseObject():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get_coordinates(self):
        kuk = [self.x, self.y, self.z]
        return kuk
        print (self.x, self.y, self.z)

class Block(BaseObject):
    def shatter(self):
        self.x = None
        self.y = None
        self.z = None

class Entity(BaseObject):
    def move(self, x1, y1, z1):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

class Thing(BaseObject):
    pass


Sheep = BaseObject(10, 5, 10)
Sheep.get_coordinates()
Sheep = Entity(3, 4, 5)
Sheep.get_coordinates()

Rock = Block(100, 235, 14)
Rock.get_coordinates()
Rock.shatter()
Rock.get_coordinates()


