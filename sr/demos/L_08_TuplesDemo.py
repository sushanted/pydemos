#Tuples are mostly heterogeneous and are immutable

simple_tuple = 1, "hi", 4.5
print(simple_tuple[1])

# In operator for checking existance
print("In:","hi" in simple_tuple)

# Deletion : del operator doesn't work : because tuples are immutable

#Tuples can be nested

nested_tuple = "one", simple_tuple, (90, 100, 101)
print(nested_tuple[1][1])
print(nested_tuple[2][2])

# Tuples can contain mutable objects
mutable_object_tuple = ([1],[2])
mutable_object_tuple[1].append(2)
print(mutable_object_tuple)

empty_tuple = ()
print(empty_tuple)

# Notice the comma : in absence of the comma it is considered as single value 1
singleton_tuple = 1,
print(singleton_tuple[0])

#Tuple unpacking : cardinality should be same at both sides
a,b,c = simple_tuple
print(a,b,c)

#Looping through tuples
for i in simple_tuple:
    print("item=",i)
# Similar to .index() on flux : enumerate returns an iterable of tuples where first item is the index
for index,i in enumerate(simple_tuple):
    print(index,":",i)

