print("\nTypes of objects AND types of classes:")


class X:
    pass


x = X()

print("type of instance x : ", type(x))
# Every (non-meta-instance) class is instance of 'type'
print("type of class X : ", type(X))

# type is class and also instance of type (instance of self)
print("type of type : ", type(type))


# A meta class is a sub-type of type
class Meta(type):
    pass


print("Meta class is also instance of type: ", type(Meta))


class MetaInstanceClass(metaclass=Meta):
    pass


# MetaInstanceClass is type of Meta instead of 'type'
print(type(MetaInstanceClass))

# We are just moving to some pre-requisites here
print("\n__new__ VS __init__:")


# __new__ and __init__ methods
# __new__ is called before __init__
class Sample:
    instance_map = {}

    # "Intercept the creation of the instance of this class"
    # It is static method, instance is not yet created
    # It is responsible for creating (or providing) an instance of the class
    # Instance can be created calling the super().__new__ OR an already created
    # instance can be provided.
    # Consider this kind of a Factory, Singleton can be implemented the same way
    def __new__(cls, *args, **kwargs):
        print("New method called with : ", cls, *args)

        if args not in cls.instance_map:
            cls.instance_map[args] = super().__new__(cls)

        return cls.instance_map[args]

    # It is instance method
    def __init__(self, name, amount):
        print("Init method called with : ", str(self.__dict__), name, amount)


salt_sample = Sample('salt', 45)
sugar_sample_1 = Sample('sugar', 10)
# This will return the same instance instead of a new
sugar_sample_2 = Sample('sugar', 10)
sugar_sample_3 = Sample('sugar', 20)

print("Is salt_sample same as suger_sample: ", salt_sample is sugar_sample_1)
print("Is sugar_sample_1 same as sugar_sample_2", sugar_sample_1 is sugar_sample_2)
print("Is sugar_sample_1 same as sugar_sample_3", sugar_sample_1 is sugar_sample_3)

print("\nMetaclass customization:")


# Python calls type(clsname,supers,attrib) to create a class reading a class definition
class X1(X):
    name = "name"


# E.g. for above class python will call type("X1",(X,),{"name":"name"})

# But if the class has a metaclass e.g. MetaClass then python calls MetaClass("X1",(X,),{"name":"name"}) to create the class


class Superb:
    pass


class MetaClass(type):
    # mcs is MetaClass : the class for which an object (which is class!) is being created
    # All other params are general constructor params (but in case of meta-class they are well defined by python)
    def __new__(mcs, class_name, super_classes, attributes):
        # Make Superb a mandatory super class of any class with this meta class
        super_classes = super_classes + (Superb,)
        print(
            f"Creating a class with name: {class_name}, with meta-class: {mcs}, "
            f"with super_classes : {super_classes} and with attributes : {attributes}")
        # type can be used directly instead of super(), but in some cases there could be a longer hierarchy
        # and the super might be interested in some aspect before calling directly the type.__new__
        return super().__new__(mcs, class_name, super_classes, attributes)

    # Note cls is already created by python at this time, cls is like self, the instance(which is a class!) just created
    # In this example it is the MetaInstance class
    def __init__(cls, class_name, super_classes, attributes):
        # Only new methods/attributes can be added or existing can be altered in __init__ (using self)
        # As cls is already created , __init__ can NOT change the super classes
        # attributes (last param to __init__) cannot be altered, they are just passed as per contract
        print(
            f"Initializing a class {cls} with name: {class_name}, with super_classes : {super_classes} "
            f"and attributes : {attributes}")
        # cls can be modified, just like a normal self in other classes (just that it is a class!)
        cls.meta_attribute = "meta_attribute_value"

    # () is done on the class : i.e. new instance of some class (having this as meta class) is being created
    # cls is the class created (MetaInstance) : the 'instance' on which __call__ is called
    # Note : the same thing can be achieved in the specific class' __new__ method, like the Sample example above.
    def __call__(cls, *args, **kwargs):
        print("Call method called, a new instance of some class having this as meta class is being created")
        # do NOT call cls() because it will cause a recursion
        # only object knows how to create a new instance finally, and it should know the class that needs to be created
        new_instance = object.__new__(cls, *args, **kwargs)
        # We just created an instance, but didn't initialize it
        # __init__ must be called as per contract of the instance creation and initialization
        new_instance.__init__(*args, **kwargs)
        return new_instance


class MetaInstance(X, metaclass=MetaClass):
    class_name = "MetaInstance"

    def __init__(self, name):
        print(f"Initialized the {type(self)} class, creating an instance named : {name}")


# At this point python will call MetaClass("MetaInstance",(X,),{"class_name":"MetaInstance"})
# It will trigger the __new__ in MetaClass and then __init__

# This will trigger __call__ in MetaClass as MetaClass is callable and
# we called it doing () on its instance :  MetaInstance()
meta_instance = MetaInstance("meta-instance-one")

# __init__ in MetaClass injected this attribute
print(meta_instance.meta_attribute)
print(isinstance(meta_instance, X))
# __new__ injected Superb as a base class for the MetaInstance class
print(isinstance(meta_instance, Superb))
