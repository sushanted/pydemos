# slicing gives a new copy of the list
# lists are mutable

the_list = [0, 1, 2, 3, 4, 5]

# in operator to check exists
print("In:", 1 in the_list)
print("Not In:", 7 not in the_list)

print("list[2]=", the_list[2])

# m to n including m excluding n
print("list[1:4]=", the_list[1:4])

# till n excluding n
print("list[:4]=", the_list[:4])

# from m including m
print("list[4:]=", the_list[4:])

# from last
print("list[-1]=", the_list[-1])

# from last-m till last -n including last-m, excluding last-n
print("list[-3:-1]=", the_list[-3:-1])

# 1 till 6 step 2
print("list[1:6:2]=", the_list[1:6:2])

# Even elements : with step 2
print("list[::2]=", the_list[::2])

# Odd elements : with step 2
print("list[1::2]=", the_list[1::2])

# concatenation : this creates a new list
print("list+[6,7]+[8]=", the_list + [6, 7] + [8])

# extend a list
the_list += [6, 7]
print("list+=[6,7]:", the_list)

# multiply a list:
print("[1,2]*3=", [1, 2] * 3)

print("\nMutations\n")

# change single item
the_list[-1] = 6;
print(the_list)

# change a slice : the size of the list can change
the_list[0:2] = [-1]
print(the_list)

the_list.append(10)
print("after append:", the_list)

# Extending with another list
the_list.extend([11, 12, 13])
# Extending with a set
the_list.extend({14, 15})
# Extending with a tuple
the_list.extend((16, 17, 18))
print("after extend:", the_list)

# make the slice empty
the_list[4:] = []
print("after emptying slice", the_list)
# Same as above
del the_list[2:]
print("after emptying slice", the_list)


# unpacking list items as args to method
def three_sum(a, b, c):
    return a + b + c


range_list = [2, 6]  # 2 to 6
print("Range from list: ", list(range(*range_list)))
print("Sum of three: ", three_sum(*[1, 2, 3]))

# length
print("length: ", len(the_list))

# Heterogeneous list
print("Heterogeneous list: ", ['a', 3, 4, 5.6])

# Nested list
print("Nested lists: ", ['a', [2, 3], the_list])

# list as stack
the_list = [1, 2, 3, 4]
the_list.append(5)
print("Popped", the_list.pop())
print("Popped", the_list.pop())
# pop item at index 0
print("Popped", the_list.pop(0))

# list methods
the_list = [1, 2, 3, 4, 5]
print("list.index(2)", the_list.index(2))
# count number of occurrences
print("list.count()", the_list.count(2))
the_list.reverse()
print("list.reverse()", the_list)
the_list.sort()
print("list.sort()", the_list)

# Looping through list
for i in the_list:
    print("item=", i)
# Similar to .index() on flux : enumerate returns an iterable of tuples where first item is the index
for index, i in enumerate(the_list):
    print(index, ":", i)

print("\nLooping through multiple sequences : ZIP \n")
# Looping through multiple lists : zip, Note: extra items are ignored
# Zip gives out a tuple
print("Zipped list items: ")
for i, a in zip([2, 4, 7], ['a', 'g', 'n', 'p']):
    print(i, a)

print("Zipped list tuples: ")
for t in zip([2, 4, 7], ['a', 'g', 'n', 'p']):
    print(t)

# There could be different types of sequences : tuple, list, set
print("Zipped tuple,list and set: ")
for t, i, a in zip((2, 3, 4), [1, 4, 7], {'a', 'b', 'c'}):
    print(t, i, a)

# Enumerate the output tuples from zip
print("Enumerated Zipped tuple,list and set tuples: ")
for index, t in enumerate(zip((2, 3, 4), [1, 4, 7], {'a', 'b', 'c'})):
    print(index, t)

print("Enumerated Zipped tuple,list and set: ")
for index, (t, i, a) in enumerate(zip((2, 3, 4), [1, 4, 7], {'a', 'b', 'c'})):
    print(index, t, i, a)

print("\nLooping order\n")
print("Reversed: ")
for i in reversed(range(0, 5)):
    print(i)

print("Sorted: ")
for i in sorted([4, 5, 2, 5, 9]):
    print(i)

print("Reversed sorted: ")
for i in reversed(sorted(range(0, 6))):
    print(i)
