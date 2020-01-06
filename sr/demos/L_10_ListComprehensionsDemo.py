
#preCursor
numbers = [1,2,3,4]
# map takes a function and an iterable, returns an iterable : result_iterable=f(input_iterable)

for i in map(lambda x:x**2,numbers):
    print(i)

# list is a terminal operation in an iterable : which returns a list : just like collect in java
# Java equivalent : numbers.stream().map(x->x**2).collect(Collectors.toList())
# this is functional representation of the operations f3(f2(f1(arg)))
print("Squares",list(map(lambda x:x**2,numbers)))

# Java equivalent : numbers.stream().filter(n->n%2==0).map(x->x**2).collect(Collectors.toList())
print("Squares of evens",list(map(lambda x:x**2,filter(lambda n:n%2==0,numbers))))

print("Comprehensions")

# This is very similar to above Square example :
#   "[]" is equivalent to list function;
#   "x**2 for x in numbers" is equivalent to map(lambda x:x**2,numbers)
print("Squares",[x**2 for x in numbers]);

print("Squares of evens",[x**2 for x in numbers if x%2==0]);

#TODO : tuples and nested comprehensions