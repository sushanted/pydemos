# Keys are always immutable objects, e.g. lists are not allowed

# Simple : JSON style

empty_dictionary = {}
simple_dictionary = {'a': 1, 'b': 20}
print(simple_dictionary)

print("a=", simple_dictionary['a'])
# Error : the key n doesn't exists
# print("n=",simple_dictionary['n'])
# way to handle :
if 'n' in simple_dictionary: print(simple_dictionary['n'])

# A safe way: this will print None if the entry doesn't exist in the dictionary
print("value of n in dictionary: ", simple_dictionary.get('n'))

# Dictionaries with string keys
string_dictionary = dict(one=1, two=2)

# Dictionary with tuple keys : composite keys : all tuple items should be immutable
tuple_dictionary = {('a', 1): 'a1', ('a', 2): 'a2', ('b', 1): 'b1'}
print("Tuple dictionary", tuple_dictionary['a', 1])

# Create dictionary from iterable giving 2-d tuples : like Java : Iterable<K,V>

print("dictionary from list of tuples:", dict([("k1", "v1"), ("k2", "v2")]))

print("dictionary from tuples of tuples:", dict((("k1", "v1"), ("k2", "v2"))))

print("dictionary from zip of sequences:", dict(zip(["k1", "k2"], ("v1", "v2"))))

print("dictionary from enumerated sequence: ", dict(enumerate(['a', 'b', 'c'])))

# In operator to check existence
print('a' in simple_dictionary)
print('d' in simple_dictionary)
print('d' not in simple_dictionary)

# Assignment/addition
simple_dictionary['b'] = 2
simple_dictionary['c'] = 3
print("After addition and change:", simple_dictionary)

# Deletion
del simple_dictionary['a']
print("After deletion:", simple_dictionary)

# Merge dictionaries
simple_dictionary.update({'a': 1})

# list of keys : in insertion order
print(list(simple_dictionary))

# Looping through dictionary key
for k in simple_dictionary:
    print("key=", k)

for a, b in tuple_dictionary:
    print("keys=", a, b)

# Looping through dictionary values
for v in simple_dictionary.values():
    print("value=", v)

# Looping through dictionary key and value
for k, v in simple_dictionary.items():
    print("key=", k, "value=", v)

for (a, b), v in tuple_dictionary.items():
    print("key=", a, b, "value=", v)


# Passing dictionary as keyword args to a function
def print_person(name, age, married):
    print("Person details: " + name + " : " + str(age) + " : " + str(married))


params = {"name": "Anukul", "married": True, "age": 23}

# Unpack a map (just like a list can be unpacked with *), make sure the param names in function are same as the keys in
# the dictionary being unpacked
print_person(**params)
