class UnitValue:
    # This is similar to static field in java
    unit_value_delimiter = " "
    default_values = []

    # This is similar to java constructor
    def __init__(self, value, unit):
        # This is similar to specifying the non static fields in Java
        self.value = value
        self.unit = unit

    def print(self):
        # Accessing fields using 'self'
        # Note: static fields can be accessed through self or using className
        # If a field with the same name as a static field is defined (using self.static_field), the non-static
        # field gets priority (it hides the static field) for that particular object instance.
        print(f"{self.value}{self.unit_value_delimiter}{self.unit}")

    def change_delimiter(self, new_delimiter):
        # unit_value_delimiter now became an instance variable
        self.unit_value_delimiter = new_delimiter


print("\nClass and instance variables\n")

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

# Mutate static values for an object and it will be changed for all objects!
# We are mutating and NOT redefining therefore it gets changed for all
uv_object_1.default_values.append(0)
print(uv_object_1.default_values)
print(uv_object_2.default_values)

# Assign static values for an object and it will change for that specific object
# We are NOT mutating but re-defining it for the particular instance
uv_object_1.default_values = [""]
print(uv_object_1.default_values)
print(uv_object_2.default_values)
