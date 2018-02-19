class SquareGeometry:
    def __init__(self,length):
        self.length=length

    def getarea(self):
        return self.length*self.length

    def getperimeter(self):
        return 4*self.length

s=SquareGeometry(2)

print(s.getarea())
print(s.getperimeter())


