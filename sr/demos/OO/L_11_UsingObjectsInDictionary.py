# Note : this is very similar to Java : the class needs to implement hash and eq method properly, then only the class
# can be used as a key in the dictionary
class CompositeKey:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash(self.age) * 31 + hash(self.name)

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name


print("\nObject Equality:\n")
print(CompositeKey('John', 32) == CompositeKey('John', 32))  # Both name and age are same
print(CompositeKey('John', 32) != CompositeKey('John', 33))  # Ages are different
print(CompositeKey('Jon', 32) != CompositeKey('John', 32))  # Names are different

print("\nObject Hashing And Equality:\n")
composite_key_dictionary = {CompositeKey('Anil', 56): 'Anil Ambani', CompositeKey('Mukesh', 63): 'Mukesh Ambani'}

print(composite_key_dictionary[CompositeKey('Anil', 56)])
print(composite_key_dictionary[CompositeKey('Mukesh', 63)])
print(CompositeKey('Mukesh', 63) in composite_key_dictionary)  # True : both name and age are same
print(CompositeKey('Mukesh', 64) in composite_key_dictionary)  # False : age is different
