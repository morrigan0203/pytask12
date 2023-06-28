

class Rectangle:
    """ Клас представляем прямоугольник """
    __slots__ = ("_length","_width")

    def __init__(self, length: int, width=None) -> None:
        """ Раширяем стандартный метод, добаляем поля length и width """
        self._length = length
        if width == None:
            self._width = length
        else:
            self._width = width
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if value >= 0:
            self._length = value

    @property
    def width(self):
        return self._width
    
    @width.setter
    def length(self, value):
        if value >= 0:
            self._width = value

    def perimetr(self):
        """ Метод расчитывает длину периметра прямоугольника """
        return 2*self._length+2*self._width
    def square(self):
        """ Метод расчитывает прощадь прямоугольника """
        return self._length*self._width

    def __add__(self, other):
        """ Переоределяем операцию сложения для прямоугольника, складываются периметры прямоугольников """
        np = self.perimetr() + other.perimetr()
        a = min(self._length, self._width, other._length, other._width)
        return Rectangle(a, (np/2)-a)

    def __sub__(self, other):
        """ Переоределяем операцию вычитания для прямоугольника, вычитаются периметры прямоугольников """
        np = abs(self.perimetr() - other.perimetr())
        a = min(self._length, self._width, other._length, other._width)
        return Rectangle(a, np/2 - a)
    
    def __str__(self) -> str:
        """ Переопределяем метод вывода в строку """
        return f'Прямоугольник с длинной {self._length} и шириной {self._width}'
    
    def __repr__(self) -> str:
        """ Переопределяем метод представления класса """
        return f'Rectangle({self._length}, {self._width})'
    
    def __eq__(self, other) -> bool:
        """ Переопределяем операцию сравнеия eq, сравниваем площади прямоугольников """
        return self.square() == other.square()

    def __ne__(self,other) -> bool:
        """ Переопределяем операцию сравнеия ne, сравниваем площади прямоугольников """
        return self.square() != other.square()

    def __gt__(self, other) -> bool:
        """ Переопределяем операцию сравнеия gt, сравниваем площади прямоугольников """
        return self.square() > other.square()

    def __ge__(self, other) -> bool:
        """ Переопределяем операцию сравнеия ge, сравниваем площади прямоугольников """
        return self.square() >= other.square()

    def __lt__(self, other) -> bool:
        """ Переопределяем операцию сравнеия lt, сравниваем площади прямоугольников """
        return self.square() < other.square()

    def __le__(self, other) -> bool:
        """ Переопределяем операцию сравнеия le, сравниваем площади прямоугольников """
        return self.square() <= other.square()
    

if __name__=="__main__":
    r = Rectangle(20,30)
    print(r.perimetr())
    print(r.square())
    r2 = Rectangle(10)
    print(r2.perimetr())
    print(r2.square())

    rs = r + r2
    print(f'{rs = }')

    rm = r - r2
    print(f'{rm = }')

    r600 = Rectangle(15, 40)
    print(f'r eq r600 = {r == r600}')
    print(f'r gt r2 = {r > r2}')
    print(f'r2 lt r = {r2 < r}')
    print(f'r nq r2 = {r != r2}')
    print(f'r ge r600 = {r >= r600}')
    print(f'r le r600 = {r <= r600}')
    print(f'r lt r600 = {r < r600}')

    print(r.__dict__)





