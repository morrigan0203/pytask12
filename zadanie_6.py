
class Positive:
    def __init__(self) -> None:
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
    
    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
    
    def validate(self, value):
        if not (type(value) == int or float):
            raise TypeError(f'Значение {value} должно быть числом')
        if value < 0:
            raise ValueError(f'Значение {value} должно быть больше 0')

class Rectangle:
    """ Клас представляем прямоугольник """
    length = Positive()
    width = Positive()

    def __init__(self, length: int, width=None) -> None:
        """ Раширяем стандартный метод, добаляем поля length и width """
        self.length = length
        if width == None:
            self.width = length
        else:
            self.width = width
    

    def perimetr(self):
        """ Метод расчитывает длину периметра прямоугольника """
        return 2 * self.length + 2 * self.width
    def square(self):
        """ Метод расчитывает прощадь прямоугольника """
        return self.length * self.width

    def __add__(self, other):
        """ Переоределяем операцию сложения для прямоугольника, складываются периметры прямоугольников """
        np = self.perimetr() + other.perimetr()
        a = min(self.length, self.width, other.length, other.width)
        return Rectangle(a, (np/2) - a)

    def __sub__(self, other):
        """ Переоределяем операцию вычитания для прямоугольника, вычитаются периметры прямоугольников """
        np = abs(self.perimetr() - other.perimetr())
        a = min(self.length, self.width, other.length, other.width)
        return Rectangle(a, np/2 - a)
    
    def __str__(self) -> str:
        """ Переопределяем метод вывода в строку """
        return f'Прямоугольник с длинной {self.length} и шириной {self.width}'
    
    def __repr__(self) -> str:
        """ Переопределяем метод представления класса """
        return f'Rectangle({self.length}, {self.width})'
    
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

    #rE = Rectangle(-10, 30)
    #r.length = -20




