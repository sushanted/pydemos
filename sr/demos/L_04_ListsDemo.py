# slicing gives a new copy of the list
# lists are mutable

list = [0,1,2,3,4,5]

print "list[2]=",list[2]

# m to n including m excluding n
print "list[1:4]=",list[1:4]

# till n excluding n
print "list[:4]=",list[:4]

#from m including m
print "list[4:]=",list[4:]

#from last
print "list[-1]=",list[-1]

#from last-m till last -n including last-m, excluding last-n
print "list[-3:-1]=",list[-3:-1]

#concatenation
print "list+[6,7]+[8]=",list+[6,7]+[8]

print "\nMutations\n"

# change single item
list[-1]=6;
print list;

# change a slice : the size of the list can change
list[0:2]=[-1];
print list;

list.append(10)
print "after append:",list

# make the slice empty
list[4:]=[]
print "after emptying slice",list

# length
print "length: ",len(list)

# Heterogeneous list
print "Heterogeneous list: ",['a',3,4,5.6]

#Nested list
print "Nested lists: ",['a',[2,3],list]




