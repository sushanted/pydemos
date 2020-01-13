import sr.demos.packaging.lib as lib, builtins

default_names = set(dir())
print("Default names",default_names)

custom_variable = 3
def custom_function():
    pass

print("custom names:",set(dir())-default_names)

print("names defined by lib:",set(dir(lib))-(default_names))

print("Builtins:",dir(builtins))