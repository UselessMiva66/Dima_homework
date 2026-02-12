#Разработайте класс Rectangle.
#
#При инициализации класс принимает два кортежа рациональных координат противоположных углов прямоугольника (со сторонами параллельными осям координат).
#
#Класс должен реализовывать методы:
#
#perimeter — возвращает периметр прямоугольника;
#area — возвращает площадь прямоугольника.
#Все результаты вычислений нужно округлить до сотых.

#Расширим функционал класса написанного вами в предыдущей задаче.
#
#Реализуйте методы:
#
#get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
#get_size() — возвращает размеры в виде кортежа;
#move(dx, dy) — изменяет положение на заданные значения;
#resize(width, height) — изменяет размер (положение верхнего левого угла остаётся неизменным).



class Rectangle:
    def __init__(self, corner1, corner2):
        self.x1,self.y1 = corner1
        self.x2, self.y2 = corner2
        self.left = min(self.x1, self.x2)
        self.right = max(self.x1, self.x2)
        self.down = min(self.y1, self.y2)
        self.top = max(self.y1, self.y2)

    def perimeter(self):
        return (self.width + self.height) * 2
    
    def area(self):
        return (self.height * self.width) // 2
    
    def get_pos(self):
        return (self.left_x, self.high_y)
    
    def get_size(self):
        return (self.width, self.height)
    
    def get_move(self, dx, dy):
        self.left_x +=dx
        self.high_y += dy

    def resize(self, width, height):
        c_left = self.left
        c_top = self.top
        self.right = c_left + width
        self.down = c_top - height
        self.x1 = self.left
        self.y1 = self.top
        self.x2 = self.right
        self.y2 = self.down
    
    def turn(self):
        new_width = self.height
        new_height = self.width
        self.left_x = new_width
        self.high_y = new_height
        self.width = new_width
        self.height = new_height


rectangle1 = Rectangle((2 , 0), (1 , 0))
print(rectangle1.perimeter())
print(rectangle1.area())
print(rectangle1.get_pos())
print(rectangle1.get_size())
rectangle1.resize(5)
print(rectangle1.get_pos())
print(rectangle1.perimeter())