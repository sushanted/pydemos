import json

print("\nSimple inheritance example\n")


class Base:
    pass


class Derived(Base):
    pass


# Arbitrary expression resolving to a class can be used for inheritance
class MyJsonEncoder(json.JSONEncoder):
    pass


class_name = Base


class NewDerived(class_name):
    pass


# Inheritance operations
print("is derived object is a base: ", isinstance(Derived(), Base))
print("is derived sub class of base: ", issubclass(Derived, Base))
print("is sub class:", issubclass(bool, int))
print("is sub class:", issubclass(int, float))

print("Method overriding")


class Rectangle:

    def area(self, height, width):
        return height * width


class Square(Rectangle):

    def area(self, side):
        # Calling overridden method, like super.area(side,side)
        return super().area(side, side)


square = Square()
print("Area of square:", square.area(5))


class Rect:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


class Sqr(Rect):

    def __init__(self, side):
        # This is kind of super(side,side) in java
        super().__init__(side, side)


sqr = Sqr(5)
print(sqr.width, " by ", sqr.height)
print("Area of square:", sqr.area())

print("\nMultiple inheritance\n")

print("\nClass methods and inheritance:")

# class method is not instance specific. but it gets the class for which it has been called

class Shape():
    _number_of_edges = 0

    def get_number_of_edges_using_instance(self):
        return self._number_of_edges

    # This is statically accessing the value defined in the Shape class, using 'Shape'
    # It has no idea from which class this method has been called
    @staticmethod
    def get_number_of_edges_static_method():
        return Shape._number_of_edges

    # The calling class is passed to a class method
    @classmethod
    def get_number_of_edges_class_method(cls):
        return cls._number_of_edges


class Circle(Shape):
    pass


class Triangle(Shape):
    _number_of_edges = 3


class Hexagon(Shape):
    _number_of_edges = 6


all_shapes = [Shape, Circle, Triangle, Hexagon]

# Works fine, but problem is : we need to create an instance of each class just to know the number of edges,
# which would be same for any given type of shape.
print("\nInstance method override:")
for shape in all_shapes:
    print(f"{shape.__name__} edges: ", shape().get_number_of_edges_using_instance())

# We can call the method using class-names
# Problem is : it prints 0 for any shape
# The static method has no idea from which class this method has been called
print("\nStatic method override:")
for shape in all_shapes:
    print(f"{shape.__name__} edges: ", shape.get_number_of_edges_static_method())

# Problem is : it prints 0 for any shape
# The static method has no idea from which class this method has been called
print("\nClass method override:")
for shape in all_shapes:
    print(f"{shape.__name__} edges: ", shape.get_number_of_edges_class_method())


# Another usage of a class method is __new__ : it will be demoed in MetaClasses Lesson