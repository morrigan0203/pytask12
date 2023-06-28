import csv

class FIO:
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
        if not (type(value) == str):
            raise TypeError(f'Значение {value} должно быть строкой')
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно быть только буквы')
        if value[0].islower():
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


class Student:
    name = FIO()
    surname = FIO()

    def __init__(self, name: str, surname: str, fileName: str) -> None:
        self.name = name
        self.surname = surname
        self.subjects = []
        self.marks = {}
        self.tests = {}
        with open(fileName, "r") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                self.subjects.append(row[0])
    
    def _validateMark(self, value):
        if type(value) != int:
            raise ValueError(f'Оценка {value} должна быть числом')
        if value < 2 or value > 5:
            raise ValueError(f'Оценка {value} должна быть от 2х до 5ти')
    
    def _validateTest(self, value):
        if type(value) != int:
            raise ValueError(f'Оценка {value} должна быть числом')
        if value < 0 or value > 100:
            raise ValueError(f'Оценка {value} должна быть от 0 до 100')
    
    def _validateSubject(self, value):
        if value not in self.subjects:
            raise ValueError(f'Предмет {value} отсутвует в списке {self.subjects}')
   
    def addMark(self, subject, mark: int):
        self._validateMark(mark)
        if subject in self.subjects:
            listMarks = self.marks.get(subject, [])
            listMarks.append(mark)
            self.marks[subject] = listMarks

    def addTest(self, subject, mark):
        self._validateTest(mark)
        if subject in self.subjects:
            listTests = self.tests.get(subject, [])
            listTests.append(mark)
            self.tests[subject] = listTests

    def allMarks(self, subject) -> list:
        self._validateSubject(subject)
        return self.marks[subject]

    def allTests(self, subject) -> list:
        self._validateSubject(subject)
        return self.tests[subject]

    def averangeMark(self):
        amount, count = 0, 0
        for k,v in self.marks.items():
            amount = amount + sum(v)
            count = count + len(v)
        return amount/count

    def averangeTests(self, subject):
        self._validateSubject(subject)
        subjectTests = self.tests[subject]
        return sum(subjectTests)/len(subjectTests)


if __name__=="__main__":

    s = Student("Вася", "Пупкин", "TesT_12/subjects.csv")
    s.addMark("Химия", 5)
    s.addMark("Химия", 4)
    s.addMark("Химия", 5)
    s.addMark("Химия", 4)
    s.addTest("Химия", 90)
    s.addTest("Химия", 100)
    s.addTest("Химия", 80)
    print(s.marks)
    print(s.averangeMark())
    print(s.averangeTests("Химия"))
