# a method or variable name starting with minimum two '_' is textually replaced by python into _ClassName__name

class Base:
    def public(self):
        self.not_to_be_overridden()
        self.__private()

    def not_to_be_overridden(self):
        print("Method not to be overridden")

    def __private(self):
        print("base private method, can't be overridden due to name mangling")

class Derived(Base):

    def __init__(self):
        self.__private_var = "private variable"

    # Accidentally overridden method
    def not_to_be_overridden(self):
        print("Method not to be overridden, but I did accidentally!!")

    # Accidentally overridden method
    def __private(self):
        print("derived private method")

derived = Derived()


print("calls accidentally overridden derived method :")
print("calls base private method and not overridden derived private method due to name mangling:")
derived.public()

print("\nCalling mangled methods:")
derived._Derived__private()
derived._Base__private()
print(derived._Derived__private_var)