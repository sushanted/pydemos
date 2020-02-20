from abc import ABC, abstractmethod

print("Python's built in mechanism for abstract classes:")


class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        print("though abstract it can have implementation common for all sub-classes, "
              "but still the concrete classes have to implement this abstract method")

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        super().abstract_method()
        print(f"{type(self).__name__} implemented abstract method : abstract_method")

class StillAbstractClass(AbstractClass):
    pass

try:
    AbstractClass()
except Exception as e:
    print("Exception : " + str(e))

try:
    StillAbstractClass()
except Exception as e:
    print("Exception : " + str(e))

ConcreteClass().abstract_method()

print("\nUnder the hood : How one can implement the abstract class mechanism:")

# Works for only single inheritance : can be modified to work with multiple inheritance
class Abstract:
    def __new__(cls, *args, **kwargs):

        complete_dict = {}

        # Replace superclass methods with methods in subclass with the same name
        for clazz in reversed([c for c in cls.mro() if c is not object]):
            complete_dict.update(clazz.__dict__)

        for name, fun in complete_dict.items():
            if isinstance(fun, AbstractMethod):
                raise Exception(f"Abstract method {name} must be implemented for class {cls.__name__}")

        return object.__new__(cls, *args, **kwargs)


class AbstractMethod:
    def __init__(self, abstract_method):
        self.abstract_method = abstract_method

    def __call__(self, *args, **kwargs):
        return self.abstract_method(*args, **kwargs)

# Marked it as abstract
class MyAbstractClass(Abstract):
    @AbstractMethod
    def my_abstract_method(self):
        pass


class MyConcreteClass(MyAbstractClass):
    def my_abstract_method(self):
        print(f"{self.__class__.__name__} Implemented the abstract method : my_abstract_method ")

    def my_concrete_method(self):
        pass

# Does NOT implement the abstract method : my_abstract_method
class MyStillAbstractClass(MyAbstractClass):
    def my_concrete_method(self):
        pass


try:
    MyAbstractClass()
except Exception as e:
    print("Exception : " + str(e))

try:
    MyStillAbstractClass()
except Exception as e:
    print("Exception : " + str(e))

MyConcreteClass().my_abstract_method()
