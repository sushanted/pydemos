print("\nTypes by scope:")

class UnitValue:
    # This is similar to static field in java
    unit_value_delimiter = " "
    default_values = []
    instance_counter = 0

    # This is similar to java constructor
    def __init__(self, value, unit):
        # This is similar to specifying the non static fields in Java
        self.value = value
        self.unit = unit
        type(self).instance_counter += 1
        print("\t\t\t\tCURRENT INSTANCES : ",type(self).instance_counter)

    def print(self):
        # Accessing attributes using 'self'
        # Note: class attributes can be accessed through self or using className
        # If an attribute with the same name as a class attribute is defined (using self.attribute), the non-class
        # attribute gets priority (it hides the class attribute) for that particular object instance.
        # The namespaces for class and instance attributes are different,
        # but the instance namespace inherits class namespace
        print(f"{self.value}{self.unit_value_delimiter}{self.unit}")

    def change_delimiter(self, new_delimiter):
        # unit_value_delimiter now became an instance variable
        self.unit_value_delimiter = new_delimiter

    def __del__(self):
        type(self).instance_counter -= 1
        print("\t\t\t\tCURRENT INSTANCES : ", type(self).instance_counter)



print("\nClass and instance variables:\n")

uv_object_1 = UnitValue(2, "cm")
uv_object_2 = UnitValue(5, "kb")

# Changed only for specific object
uv_object_1.unit = "m"
uv_object_1.print()
uv_object_2.print()

# Static field : Changed for all objects : using name of the class
UnitValue.unit_value_delimiter = " => "
uv_object_1.print()
uv_object_2.print()

# Static field : Changed(re-defined) for specific object as it now becomes instance field : using name of the object
uv_object_1.unit_value_delimiter = ":"
uv_object_1.print()
uv_object_2.print()

# Static field : Changed(re-defined) for specific object : using mutator method
uv_object_2.change_delimiter("_")
uv_object_1.print()
uv_object_2.print()

# Mutate class values for an object and it will be changed for all objects!
# We are mutating and NOT redefining therefore it gets changed for all
uv_object_1.default_values.append(0)
print(uv_object_1.default_values)
print(uv_object_2.default_values)

# Assign class values for an object and it will change for that specific object
# We are NOT mutating but re-defining it for the particular instance
uv_object_1.default_values = [""]
print(uv_object_1.default_values)
print(uv_object_2.default_values)



print("\nTypes by visibility:")

# Naming    Type        Meaning
# name      Public      These attributes can be freely used inside or outside of a class definition.
# _name	    Protected   Protected attributes should not be used outside of the class definition, unless inside of a subclass definition.
# __name	Private     This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside of the class definition itself.

class A():
    def __init__(self):
        self.__private = 'private'
        self.__protected = 'protected'
        self.public = 'public'

a = A()
#print(a.__private) # Cannot access
#print(a._protected) # Cannot access
print(a.public) # can be accessed

print("\nStatic and class methods:")



class StaticInfoClass():

    __info = 'This is a static information'

    # This is a non static method, an instance is always needs to be passed as first arg, can  NOT be called using only classname
    def get_info(self):
        return StaticInfoClass.__info;

    def get_info_only_statically():
        return StaticInfoClass.__info;

    # This is now a static method, can be called using an instance or class name
    # This doesn't need(should not have) the first param as self
    @staticmethod
    def get_static_info():
        return StaticInfoClass.__info;




static_info_object = StaticInfoClass()

print(static_info_object.get_info())
# This will NOT work because get_info is not static, and get_info() expects the first param as self
#print(StaticInfoClass.get_info())

print(StaticInfoClass.get_info_only_statically())
# This will NOT work because get_info_only_statically doesn't accept any arg (but self get passed)
#print(static_info_object.get_info_only_statically())

# Both of the following will work because get_static_info is static
print(static_info_object.get_static_info()) # self will be ignored
print(StaticInfoClass.get_static_info()) # self is not anyways expected!









