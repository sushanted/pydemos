# iterators : the for statement calls iter() on the container object.
# The function returns an iterator object that defines the method __next__() which accesses elements in the
# container one at a time. When there are no more elements, __next__() raises a StopIteration exception which tells
# the for loop to terminate.

for ch in "string":
    print(ch)

print("Accessing items using for loop:")
for item in (1, 3, 4):
    print(item)

# Behind the scene:
iterator = (1, 3, 4).__iter__()
print("Accessing items using raw iterator (this is what for loop does behind the scene)")
done = False
while (not done):
    try:
        print(iterator.__next__())
    except StopIteration:
        done = True

print("\nCustom iterator implementation :\n")


class Squares:
    def __init__(self, upto):
        self.upto = upto
        # First value is the last square number
        # Second value is current difference between consecutive square numbers
        self.square_state = dict(last_square_number=0, current_difference=1)

    def __iter__(self):
        return self

    def __next__(self):
        self.square_state = dict(
            last_square_number=self.square_state["last_square_number"] + self.square_state["current_difference"],
            current_difference=self.square_state["current_difference"] + 2
        )
        if self.square_state["last_square_number"] > self.upto:
            raise StopIteration
        return self.square_state["last_square_number"]


print("Squares upto 5:")
for i in Squares(5):
    print(i)

print("Squares upto 101:")
for i in Squares(101):
    print(i)

print("\nGenerator:\n")


# With generators there is no need to write iterators methods : __next__ , no need to maintain interim state,
# and no need to check the end of iteration and raise StopIteration
def reverse_squares():
    for i in range(10, 0, -1):
        # yield should always be in a function
        yield i * i


print("Reversed squares")
for i in reverse_squares():
    print(i)


# Same example as that of iterator (without state maintenance)
def squares(upto):
    last_square_number = 0
    current_difference = 1
    while (last_square_number + current_difference) < upto:
        last_square_number = last_square_number + current_difference
        current_difference = current_difference + 2
        yield last_square_number


print("Squares upto 101")
for i in squares(101):
    print(i)

print("\nGenerator expressions:\n")
# This are similar to list comprehensions, but don't create and intermediate list, but directly an iterable (saving on memory)

# Comprehension
print("Sum of first 10 numbers:", sum([i for i in range(1, 11)]))
# Equivalent Generator expression
print("Sum of first 10 numbers:", sum(i for i in range(1, 11)))

# Similar example as that of function based generator now using generator expression
number_of_squares_to_generate = 10
last_square_number = 0
print(*(last_square_number := last_square_number + current_difference for current_difference in
        range(1, number_of_squares_to_generate * 2, 2)))

# Note 1: := is walrus operator : assignment inside an expression
# Note 2: *iterable : unpacks the iterable into the evaluated values
