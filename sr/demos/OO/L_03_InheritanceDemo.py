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
        return Rectangle.area(self, side, side)


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
        Rect.__init__(self, side, side)


sqr = Sqr(5)
print(sqr.width, " by ", sqr.height)
print("Area of square:", sqr.area())

print("\nMultiple inheritance\n")


# Classic diamond hierarchy
class Top:
    def print(self):
        print("center")

    def top_print(self):
        print("center_print")


class Left(Top):
    def print(self):
        Top.print(self)
        print("left")

    def left_print(self):
        print("left_print")


class Right(Top):
    def print(self):
        Top.print(self)
        print("right")

    def right_print(self):
        print("right_print")


class BottomLR(Left, Right):
    pass


class BottomRL(Right, Left):
    pass


for cls in (BottomLR, BottomRL):
    ob = cls()
    print(f"For class: {ob.__class__} with inheritance order: {ob.__class__.__bases__}")
    # The print method is found bottom to top, left to right manner
    # The output depends on the class for LR Left.print is found first, for RL Right.print is found first
    ob.print()
    # All inherited methods are available
    ob.top_print()
    ob.left_print()
    ob.right_print()
