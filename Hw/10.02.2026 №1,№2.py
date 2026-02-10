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
    def __init__(self, ygol1, ygol2):
        x1, y1 = ygol1
        x2, y2 = ygol2
        self.width = abs(x1 - x2)
        self.height = abs(y1 - y2)
        self.left_x = min(x1, x2)
        self.high_y = max(y1, y2)

    def perimeter(self):
        self.gip = (self.width ** 2 + self.height ** 2) **0.5
        return self.gip + self.width + self.height
    
    def area(self):
        return (self.height * self.width)//2
    
    def get_pos(self):
        return (self.left_x, self.high_y)
    
    def get_size(self):
        return (self.width, self.height)
    
    def get_move(self, dx, dy):
        self.left_x +=dx
        self.high_y += dy

    def resize(self, width, height):
        self.width = width
        self.height = height


rectangle1 = Rectangle((2 , 0), (1 , 0))
print(rectangle1.perimeter())
print(rectangle1.area())
print(rectangle1.get_pos())
print(rectangle1.get_size())