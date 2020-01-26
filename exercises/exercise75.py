class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.length = 1

    def area(self):
        return self.length*self.length

square = Square()
print(square.area())

# The exercise requires understanding on class and its inheritance
# The soultion for exercise relates to examples of class exercises which will be written below.


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the print

x = Person('John', 'Doe')
x.printname()



class Student(Person):
    pass

x = Student("Mike", "Owen")
x.printname()
