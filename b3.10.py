pi=3.14
def _inter_(self, radius=1):
    self.radius=radius
def _setradius_(self, radius):
    selt.radius=radius
def _getradius_(self):
    return  self.radius
def area(self):
    return self.radius*self.radius*self.pi
#bat dau
a = hinhtron()
dt = a.area()
print(dt)
b= Hinhtron()
b.setRadius(5)
print(b.area())