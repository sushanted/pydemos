import math

print("\nEverything is an object, even primitives\n")

print(type(True))
print(type(5))
print(type('str'))
print(type(['x']))

def fun(): pass

print(type(fun)) # class: function

print(type(math)) # class: module

print("\nSimple class definition\n")


# A simple class definition
class SimpleClass:
    # Class level variable (like static in Java)
    world = "world"

    # Method definition
    # It must take first argument as self, consider self as class's namespace
    def hello(self):
        print("Hello " + self.world)


# Object(Instance) creation
simple_class_object = SimpleClass()
# calling method
simple_class_object.hello()

print("\nClass with constructor and destructor\n")


class UnitValue:
    # This is similar to static field in java
    unit_value_delimiter = " "

    # This is similar to java constructor
    def __init__(self, value, unit):
        # This is similar to specifying the non static fields in Java
        self.value = value
        self.unit = unit

    def print(self):
        print(f"{self.value}{UnitValue.unit_value_delimiter}{self.unit}")

    # This is called if object is explicitly deleted with del or at the end of the scope
    def __del__(self):
        print("Destroyed UnitValue")

    # methods must have first arg as self else it doesn't compile
    # def static():
    # pass


unit_value_object = UnitValue(5, "kg")
# fields can be directly accessed with . notion
print("Value:", unit_value_object.value)
unit_value_object.value = 9
# calling methods
unit_value_object.print()

# deleting
uvo = UnitValue(3,"mb")
print("Trying to destroy...")
del uvo

def use_uv():
    uvo = UnitValue(3, "mb")

print("Using uv")
use_uv()
print("Use over, uv already have been destroyed")

# Needs an object as a param (compare with UnitValue::print in java)
generic_print = UnitValue.print
print("Generic print function")
generic_print(unit_value_object)

# Doesn't need an object as a param, object param is already embedded (compare with unit_value_object::print in java)
instance_print = unit_value_object.print
print("Object print function")
instance_print()

print("Get class object from an instance using type")
type(unit_value_object).print(unit_value_object)

# Way to obtain the function object from method object (can be used to operate on another instance)
function_object = instance_print.__func__
function_object(unit_value_object)

# Way to get the instance object from method object
unit_value_object_reference = instance_print.__self__
unit_value_object_reference.print()



print("\nArbitrary fields and methods\n")

# An arbitrary field for a class can be introduced at any time
unit_value_object.type = "scalar"
print(unit_value_object.type)



def uv_print(self):
    print(f"{self.value}{self.unit_value_delimiter}{self.unit}({self.type})")


# An arbitrary method can be introduced for the class at any time : NOT A GOOD PRACTICE
UnitValue.uv_print = uv_print
unit_value_object.uv_print()

print("\ngetattr and setattr:\n")

# Generically get attribute or default value
print(getattr(unit_value_object,"type",None))
print(getattr(unit_value_object,"undefined_attribute","default value"))
setattr(unit_value_object,"new_attr",5)
print(getattr(unit_value_object,"new_attr",-1))


print("Class of the object: ", unit_value_object.__class__)

