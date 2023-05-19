class Point:
    def __init__(self, x=0, y=0): # 파라미터의 기본값
        self.__x = x
        self.__y = y

    def set(self, x, y):
        self.__x = x
        self.__y = y
    
    def get(self):
        return (self.__x, self.__y)

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def show(self):
        print(f"좌측 상단 꼭지점이 ({self.x1},{self.y1})이고 우측 상단 꼭지점이 ({self.x2},{self.y2})인 사각형입니다.")

    def getWidth(self):
        width = self.x2-self.x1
        return width
    def getHeight(self):
        height = self.y2 - self.y1
        return height
    def getArea(self):
        area = self.getWidth()*self.getHeight()
        return area
    def getPerimeter(self):
        perimeter = 2*(self.getWidth() + self.getHeight())
        return perimeter

r1 = Rectangle(5, 5, 20 ,10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f"넓이는 {a}, 둘레는 {p}")