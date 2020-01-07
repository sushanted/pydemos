# Keys are always immutable objects, e.g. lists are not allowed

# Simple : JSON style
from builtins import tuple

empty_dictionary ={}
simple_dictionary = {'a':1,'b':20}
print(simple_dictionary)
print("a=",simple_dictionary['a'])
# Error : the key n doesn't exists
#print("n=",simple_dictionary['n'])
# way to handle :
if 'n' in simple_dictionary: print(simple_dictionary['n'])

# Another type of construction : list of tuples
another_dictionary = dict([('a',1),('b',2)])
print("Another dictionary:",another_dictionary)

# Dictionaries with string keys
string_dictionary=dict(one=1,two=2)

# Dictionary with tuple keys : composite keys : all tuple items should be immutable
tuple_dictionary={('a',1):'a1',('a',2):'a2',('b',1):'b1'}
print("Tuple dictionary",tuple_dictionary['a',1])

# In operator to check existence
print('a' in simple_dictionary)
print('d' in simple_dictionary)
print('d' not in simple_dictionary)

# Assignment/addition
simple_dictionary['b']=2
simple_dictionary['c']=3
print("After addition and change:",simple_dictionary)

# Deletion
del simple_dictionary['a']
print("After deletion:",simple_dictionary)

# list of keys : in insertion order
print(list(simple_dictionary))

#Looping through dictionary key
for k in simple_dictionary:
    print("key=",k)

for a,b in tuple_dictionary:
    print("keys=",a,b)

#Looping through dictionary key and value
for k,v in simple_dictionary.items():
    print("key=",k,"value=",v)

for (a,b),v in tuple_dictionary.items():
    print("key=",a,b,"value=",v)

