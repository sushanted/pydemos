# Tuples are mostly heterogeneous and are immutable

simple_tuple = 1, "hi", 4.5
print(simple_tuple[1])

# In operator for checking existance
print("In:", "hi" in simple_tuple)

# Deletion : del operator doesn't work : because tuples are immutable

# Tuples can be nested

nested_tuple = "one", simple_tuple, (90, 100, 101)
print(nested_tuple[1][1])
print(nested_tuple[2][2])

# Tuples can contain mutable objects
mutable_object_tuple = ([1], [2])
mutable_object_tuple[1].append(2)
print(mutable_object_tuple)

empty_tuple = ()
print(empty_tuple)

# Notice the comma : in absence of the comma it is considered as single value 1
singleton_tuple = 1,
print(singleton_tuple[0])

# Tuple unpacking : cardinality should be same at both sides
a, b, c = simple_tuple
print(a, b, c)

# Looping through tuples
for i in simple_tuple:
    print("item=", i)
# Similar to .index() on flux : enumerate returns an iterable of tuples where first item is the index
for index, i in enumerate(simple_tuple):
    print(index, ":", i)


def concatenate(a, b, c):
    return f"{a}:{b}:{c}"


# Unpack a tuple just like list
print(concatenate(*simple_tuple))

# Transposing a list of tuples
original_tuple = (('a','b','c','d'),(1,2,3,4))

# * passes unpacked list to zip, zip will get two arguments: ('a','b','c','d'),(1,2,3,4) , which are tuples
# Now zip will pick elements one by one from each input tuple to create pairs of tuples
# list again creates list from the items provided by the zip
# * now unpacks the list into a tuples
print("Transposed tuples:",*list(zip(*original_tuple))) #('a', 1) ('b', 2) ('c', 3) ('d', 4)


t1 = (1,2)
t2 = (3,4)
# Creates a new immutable tuple as concatenation of two tuples
print(t1+t2)


# convert iterables into tuple
a,b,c = tuple([i for i in range(3)])
print(a,b,c)

# this is more simple, direct assign an array of length n to n variable tuple
a,b,c = [i for i in range(3)]
print(a,b,c)

# multiple iterables (a list a set and a tuple) into multiple tuples
(a,b,c),(d,e,),(f,g,h) = [3,4,5],{6,7},(8,9,10)
print(a,b,c,d,e,f,g,h)

# iterable to tuple : tuple including a catch-all element
start,*values,end = range(10)
print(f"from {start} to {end}, values: {values}")

# An interesting example : converting an iterable into a list
# Note that the list is part of the tuple on LHS
*the_list, = (1,2,3)
print(the_list)