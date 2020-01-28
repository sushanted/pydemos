import copy

class Org:
    def __init__(self,name,sub_org):
        self.name = name
        self.sub_org = sub_org

    # This is like toString in Java
    def __str__(self):
        return "name:"+self.name+"\nsub_org:\n\t"+str(self.sub_org)


original_org = Org("a",Org("a-sub",None))

print("Original org before copy:\n")
print(str(original_org))

copied_org = copy.deepcopy(original_org) # copy.copy does only shallow copy
copied_org.name = "b"
copied_org.sub_org.name = "b-sub"

print("Original org after copy:\n")
print(str(original_org))

print("Copied org:\n")
print(str(copied_org))