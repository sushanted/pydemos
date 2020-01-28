# Empty set, "{}" creates an empty dictionary not a set
empty_Set = set()
print(empty_Set)

# Set is always sorted
simple_set = {6, 1, 2, 3, 4, 3, 2, 1}

# Values will be printed sorted
print(simple_set)

# in operator on set
print("In:", 1 in empty_Set)
print("In:", 1 in simple_set)
print("In:", 7 not in simple_set)

# deletion
# del operator doesn't work on sets
# del simple_set[1]
simple_set.remove(1)
print("After deletion:", simple_set)

# addition
simple_set.add(9)
print("After addition:", simple_set)

# set of chars from words: set function only works on iterables
print(set("hello"))
print(set(range(3, 6)))
print(set(['one', 'two', 'one', 'three']))

# set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set difference:", a - b)
print("Set union:", a | b)
print("Set intersection:", a & b)
print("Set uncommon: (a|b)-(a&b)", a ^ b)

print("is subset: ", {1, 2}.issubset(a))
print("is super set: ", a.issuperset({1, 2}))
print("is disjoint: ", a.isdisjoint({5, 6, 7}))

# Looping through set
for i in simple_set:
    print("item=", i)
# Similar to .index() on flux : enumerate returns an iterable of tuples where first item is the index
for index, i in enumerate(simple_set):
    print(index, ":", i)


# unpacking set items as args to method
def concatenate(a, b, c):
    return f"{a}:{b}:{c}"


# Note : the arguments will be passed sorted to the function
print("Concatenated: ", concatenate(*{3, 2, 1}))  # 1:2:3

print("\nFrozen set: Immutable set:\n")

frozen_set = frozenset([1, 2, 3])
# Following won't work on a frozen set
# frozen_set.remove(2)
# frozen_set.add(3)
