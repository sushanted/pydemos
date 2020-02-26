
# Static class creation
class A1:
    pass

# Dynamic class creation
A2 = type("A2",(),{})

a1 = A1()
a2 = A2()

print(f"type of A1 {type(a1)}, type of A2 {type(a2)}")

# Complex class creation

class B1(A1):
    class_name = "B1"

    def __init__(self,value):
        self.attrib = value

    def __str__(self):
        return self.class_name + " : " + self.attrib

# Any reference to method can be assigned
B2 = type("B2",(A2,),{"class_name":"B2","__init__": B1.__init__,"__str__":B1.__str__})

print(str(B1("hello static")))
print(str(B2("hello dynamic")))


# NOTE : python creates the class reading the definition and calling : type(name,supers,attribs)