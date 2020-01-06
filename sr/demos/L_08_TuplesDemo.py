#Tuples are mostly heterogeneous and are immutable

t = 1,"hi",4.5
print(t[1])

#Tuples can be nested

nested_tuple = ("one",t,(90,100,101))
print(nested_tuple[1][1])
print(nested_tuple[2][2])

# Tuples can contain mutable objects
mutable_object_tuple = ([1],[2])
mutable_object_tuple[1].append(2)
print(mutable_object_tuple)

empty_tuple = ()
print(empty_tuple)

# Notice the comma : in absence of the comma it is considered as single value 1
singleton_tuple = (1,)
print(singleton_tuple[0])

#Tuple unpacking : cardinality should be same at both sides
a,b,c = t
print(a,b,c)

