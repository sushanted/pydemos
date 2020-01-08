# preCursor
numbers = [1, 2, 3, 4]
# map takes a function and an iterable, returns an iterable : result_iterable=f(input_iterable)

for i in map(lambda x: x ** 2, numbers):
    print(i)

# list is a terminal operation in an iterable : which returns a list : just like collect in java
# Java equivalent : numbers.stream().map(x->x**2).collect(Collectors.toList())
# this is functional representation of the operations f3(f2(f1(arg)))
print("Squares", list(map(lambda x: x ** 2, numbers)))

# Java equivalent : numbers.stream().filter(n->n%2==0).map(x->x**2).collect(Collectors.toList())
print("Squares of evens", list(map(lambda x: x ** 2, filter(lambda n: n % 2 == 0, numbers))))

print("\nComprehensions\n")

# This is very similar to above Square example :
#   "[]" is equivalent to list function;
#   "x**2 for x in numbers" is equivalent to map(lambda x:x**2,numbers)
print("Squares", [x ** 2 for x in numbers]);

# Rule of thumb : comprehension syntax is equivalent to following:
# [ expression_involving_variables for X for Y if Z]
# the_list = []
# for X
#    for Y
#       if Z
#           the_list.append(expression_involving_variables)


print("Squares of evens", [x ** 2 for x in numbers if x % 2 == 0]);

# Equivalent simple code for above comprehension:
squares_of_evens = []
for x in numbers:
    if x % 2 == 0:
        squares_of_evens.append(x ** 2)

print("Combinations of blood groups:", [(group, sign) for group in ['A', 'B', 'AB', 'O'] for sign in ['+', '-']])

# Equivalent simple code for above comprehension:
blood_group_combinations = []
for group in ['A', 'B', 'AB', 'O']:
    for sign in ['+', '-']:
        blood_group_combinations.append((group, sign))

list_2d = [[1, 2, 3], [4, 5], [6]]
# Flatten a list
print("Flattened list:", [number for innner_list in list_2d for number in innner_list])

print("\nNested comprehensions\n")

print("Tables:", [[x * y for y in range(1, 6)] for x in range(1, 6)])

# Equivalent simple code for above comprehension:
tables = []
for x in range(1, 6):
    tables.append([x * y for y in range(1, 6)])

# Set comprehensions
print("Evens set:", {x // 2 for x in range(0, 10)})

# Dictionary comprehensions
print("Square map: ", {x: x * x for x in range(0, 5)})
