import math


class ValidationDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, number):
        if number < 0:
            raise ValueError('Invalid value!')
        return self.func(number)


print("\nDynamic decoration\n")

decorated_log2 = ValidationDecorator(math.log2)

print(decorated_log2(32))  # This is equivalent to calling the __call__ method on ValidationDecorator instance

print("\nStatic decoration\n")


# Equivalent static decoration
# square = ValidationDecorator(square)
# square(value) is now equivalent to ValidationDecorator(square)(value) i.e. ValidationDecorator(square).__call__(value)
# Here we provided the class name to python,
# Python will call ClassName(square) i.e. ClassName.__init__(square) to get the decorator
@ValidationDecorator
def square(value):
    return value ** 2


try:
    print(square(-3))
except ValueError as v:
    print("Invalid input: " + str(v))

print("\nParameterized class decorator:\n")


class ParamLogger:

    def __init__(self, print_params):
        self.print_params = print_params

    # Note here __call__ is accepting a function as input (earlier example had __init__ accepting a function)
    def __call__(self, func):
        def decorator(number):
            print(
                f"Decorated function {func.__name__} {'called with args: ' + str(number) if self.print_params else ''}")
            return func(number)

        return decorator


# ParamLogger(True) returns a callable class instance: which is equivalent to a callable instance
# The call method in class accepts a function and returns a decorator
# Equivalent code:
# paramLogger = ParamLogger(True)
# cube = paramLogger(cube) # paramLogger.__call__(cube)
# Here we called the constructor to get an instance and provided that instance to python
# Python will call instance(cube) i.e. instance.__call__(cube) to get the decorator
@ParamLogger(True)
def cube(value):
    return value ** 3


@ParamLogger(False)
def power4(value):
    return value ** 4


print(cube(5))
print(power4(2))


# Decorating a class
class StrAdder():

    def to_string(object):
        to_string = ""
        for key, value in object.__dict__.items():
            to_string += str(key) + " : " + str(value) + "\n"

        return to_string

    def __init__(self, cls):
        print("Decorating class: " + str(cls))
        self.cls = cls
        # add __str__ method dynamically to the passed class
        cls.__str__ = type(self).to_string

    def __call__(self, *args, **kwargs):
        # Create an instance of cls class and return
        return self.cls(*args, **kwargs)

# Decoration : PersonalInfo = StrAdder(PersonalInfo)
# Now while creating an instance of PersonalInfo, PersonalInfo(name,age) will be called,
# i.e. StrAdder(PersonalInfo)(name,age) will be called
#
@StrAdder
class PersonalInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age


@StrAdder
class Student:
    def __init__(self, clazz, marks, personalInfo):
        self.clazz = clazz
        self.marks = marks
        self.personalInfo = personalInfo


pi = PersonalInfo("Deepak", 45)

print(str(pi))

student = Student("second", 34, pi)

print(str(student))
