# slicing gives a new copy of the list
# lists are mutable

the_list = [0, 1, 2, 3, 4, 5]

print("list[2]=", the_list[2])

# m to n including m excluding n
print("list[1:4]=", the_list[1:4])

# till n excluding n
print("list[:4]=", the_list[:4])

#from m including m
print("list[4:]=", the_list[4:])

#from last
print("list[-1]=", the_list[-1])

#from last-m till last -n including last-m, excluding last-n
print("list[-3:-1]=", the_list[-3:-1])

#concatenation
print("list+[6,7]+[8]=", the_list + [6, 7] + [8])

print("\nMutations\n")

# change single item
the_list[-1]=6;
print(the_list)

# change a slice : the size of the list can change
the_list[0:2]=[-1]
print(the_list)

the_list.append(10)
print("after append:", the_list)

# make the slice empty
the_list[4:]=[]
print("after emptying slice", the_list)
# Same as above
del the_list[2:]
print("after emptying slice", the_list)

#unpacking list items as args to method
def three_sum(a,b,c):
    return a+b+c

range_list = [2,6] # 2 to 6
print("Range from list: ",list(range(*range_list)))
print("Sum of three: ",three_sum(*[1,2,3]))

# length
print("length: ", len(the_list))

# Heterogeneous list
print("Heterogeneous list: ",['a',3,4,5.6])

#Nested list
print("Nested lists: ", ['a', [2,3], the_list])



#list as stack
the_list = [1, 2, 3, 4]
the_list.append(5)
print("Popped", the_list.pop())
print("Popped", the_list.pop())
#pop item at index 0
print("Popped", the_list.pop(0))

#list methods
the_list=[1, 2, 3, 4, 5]
print("list.index(2)", the_list.index(2))
# count number of occurrences
print("list.count()", the_list.count(2))
the_list.reverse()
print("list.reverse()", the_list)
the_list.sort()
print("list.sort()", the_list)






