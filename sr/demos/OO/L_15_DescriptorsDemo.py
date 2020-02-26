print("\nDescriptor protocol")

# Data-Descriptor is a class which implements any of __get__ and ( __set__ or __delete__) methods

# Whenever a class level attribute is accessed using an instance (e.g. class_instance.attr) and the attribute (attr)
#  is already an instance of a descriptor class , attr.__get__(class_instance,class) is called
#  and the return value of __get__ is returned to the accessor.

# Whenever a class level attribute is assigned using an instance (e.g. class_instance.attr = new_value) and
#  the attribute (attr) is already an instance of a descriptor class , attr.__set__(class_instance,value) is called

# Whenever a class level attribute is deleted using an instance (e.g. del class_instance.attr) and the attribute (attr)
#  is already an instance of a descriptor class , attr.__delete__(class_instance) is called


print("A sample descriptor:")


class LoggingDescriptor:

    def __init__(self, property_name):
        print(f"Descriptor got created for property : {property_name}")
        self.property_name = property_name

    # Note : the instance is the instance of the class for which the attribute is being set
    # owner is the class : useful in inheritance
    def __get__(self, instance, owner):
        print(f"Somebody asked for the value for {self.property_name} using class {owner}")
        if not instance:
            print("But didn't provide an instance!")
            return None
        return instance.__dict__.get(self.property_name)

    def __set__(self, instance, value):
        print(f"Somebody is changing the value for {self.property_name} with {value}")
        instance.__dict__[self.property_name] = value

    def __delete__(self, instance):
        print(f"Somebody is deleting value for {self.property_name}")
        del instance.__dict__[self.property_name]


class Person:
    # Note the descriptors are always assigned to class level attributes, but come into action when those attributes
    # are accessed/assigned/deleted using instance of the class (OR accessed through class name)
    # Also note that : We have created a separate descriptor for each attribute
    name = LoggingDescriptor("name")
    age = LoggingDescriptor("age")

    def __init__(self, name, age):
        # descriptors __set__ will be called with instance=self and value={name}/{age}
        self.name = name
        self.age = age


ajay = Person("Ajay", 45)
vijay = Person("Vijay", 23)

# calls the descriptors __get__
print(ajay.name)
# calls the descriptors __set__(ajay,53)
ajay.age = 53
# calls the descriptors __get__(ajay,Person)
print(ajay.name, ajay.age)
# calls the descriptors __delete__(ajay)
del ajay.name, ajay.age

print(ajay.name, ajay.age)

print("\n")
# different person will have different values for properties (as we store the values in instance.__dict__)
print(vijay.name, vijay.age)

print("\nUsing descriptors for encapsulations (what we actually do in getter/setter in java)")


class AgeValidationDescriptor:
    property_name = 'age'

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.property_name)

    def __set__(self, instance, age):
        if age < 0 or age > 150:
            raise ValueError('Age should be between 0 to 150')
        instance.__dict__[self.property_name] = age


class NameDescriptor:
    property_name = 'name'

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.property_name)

    def __set__(self, instance, name):
        if self.property_name in instance.__dict__:
            raise ValueError("Name already set")
        instance.__dict__[self.property_name] = name


class ValidPerson:
    name = NameDescriptor()
    age = AgeValidationDescriptor()

    def __str__(self):
        return f"{self.name}({self.age})"


pradeep = ValidPerson()

pradeep.name = 'Pradeep'
pradeep.age = 23

print("Valid person: ", pradeep)

# Now let's break the rules
try:
    print("Trying to reset the name of the person:")
    pradeep.name = 'Akshay'
except ValueError as v:
    print(v)

try:
    print("Trying to set a negative age:")
    pradeep.age = -45
except ValueError as v:
    print(v)

print("Person still valid: ", pradeep)

# Above code style looks good for generic descriptors like logging, timing etc, but not suitable
# for specific encapsulation, it looks overkill to create a new descriptor for each attribute
print("\nUsing descriptors like java style:")


class GenericDescriptor:

    def __init__(self,  __getter=None,__setter=None, __deleter=None):
        self.__setter = __setter
        self.__getter = __getter
        self.__deleter = __deleter

    def __set__(self, instance, value):
        self.__setter(instance, value)

    def __get__(self, instance, owner):
        return self.__getter(instance)

    def __delete__(self, instance):
        return self.__deleter(instance)

    def setter(self, __setter):
        self.__setter = __setter
        return self  # should return the descriptor as the decorator


class GenuinePerson:

    def __init__(self):
        self.__name = None

    # Note: now the encapsulation code is inside the class itself

    # This is the getter like getName() in java
    # This will call GenericDescriptor(name), name as first param i.e. getter
    # now name = GenericDescriptor(name)
    # i.e. name is a descriptor AND instance.name  will call __get__(instance)
    @GenericDescriptor
    def name(self):
        return self.__name

    # This is the setter like setName() in java
    # This will call name.setter(name) ; remember name was descriptor as set in the above code
    # we are calling the same descriptor's setter method passing this method : name.setter(name)
    # the descriptors setter method returns the descriptor's instance again
    # so this another name is also the same descriptor instance
    # i.e. name is a descriptor AND instance.name = 'x' will call __set__(instance,'x')
    @name.setter
    def name(self, value):
        if self.__name:
            raise ValueError("Name already set")
        self.__name = value

    @GenericDescriptor
    def age(self):
        return self.__age

    @age.setter
    def age(self, age_value):
        if age_value < 0 or age_value > 150:
            raise ValueError('Age should be between 0 to 150')
        self.__age = age_value

    def __str__(self):
        return f"{self.name}({self.age})"


suraj = GenuinePerson()
suraj.name = "Suraj"
suraj.age = 56
print("Genuine person :", suraj)

# Now let's break the rules
try:
    print("Trying to reset the name of the person:")
    suraj.name = 'Akshay'
except ValueError as v:
    print(v)

try:
    print("Trying to set a negative age:")
    suraj.age = -45
except ValueError as v:
    print(v)

print("Person still valid: ", suraj)

print("\nUsing Property:")

class PerfectPerson:

    def __init__(self):
        self.__name = None
        self.__age = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,__name):
        if self.__name:
            raise ValueError("Name already set")
        self.__name = __name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,__age):
        if __age < 0 or __age > 150:
            raise ValueError('Age should be between 0 to 150')
        self.__age = __age

    def __str__(self):
        return f"{self.name}({self.age})"

pankaj = PerfectPerson()
pankaj.name = "Pankaj"
pankaj.age = 43
print("Perfect person :", pankaj)

# Now let's break the rules
try:
    print("Trying to reset the name of the person:")
    pankaj.name = 'Akshay'
except ValueError as v:
    print(v)

try:
    print("Trying to set a negative age:")
    pankaj.age = -45
except ValueError as v:
    print(v)

print("Person still valid: ", pankaj)