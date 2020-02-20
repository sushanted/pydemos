print("\n Basic str and repr example:")


class Person:
    def __init__(self, name, age, phones):
        self.name = name
        self.age = age
        self.phones = phones

    # Human readable format
    def __str__(self):
        return f"{self.name}({self.age}){self.phones}"

    # Python parsable format : Person('Nitin',45,[421324, 46355])
    def __repr__(self):
        return f"Person({repr(self.name)},{repr(self.age)},{repr(self.phones)})"


person = Person('Nitin', 45, [421324, 46355])
print(person)

person_repr = repr(person)

print(person_repr)
# Eval should be able to parse from repr of an object
copy_person = eval(person_repr)

print(copy_person)

# The code inside repr will get printed as is
print(repr([(1, 2), {3, 4}, {'x': 45}]))

# The rule : Human can read machine repr but machine cannot read human str
print("\nstr without repr")


class OnlyStr:
    def __str__(self):
        return "OnlyStr"


print(str(OnlyStr()))
print(repr(OnlyStr()))  # this does NOT calls str

print("\nrepr without str")


class OnlyRepr:
    def __repr__(self):
        return "OnlyRepr()"


print(str(OnlyRepr()))  # this calls repr as str is not defined
print(repr(OnlyRepr()))
