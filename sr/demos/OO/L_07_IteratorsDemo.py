# iterators : the for statement calls iter() on the container object.
# The function returns an iterator object that defines the method __next__() which accesses elements in the
# container one at a time. When there are no more elements, __next__() raises a StopIteration exception which tells
# the for loop to terminate.

for ch in "string":
    print(ch)

print("Accessing items using for loop:")
for item in [1, 3, 4]:
    print(item)

# Behind the scene:
iterator = iter([1, 3, 4]) # This is like calling [1,3,4].__iter__
print("Accessing items using raw iterator (this is what for loop does behind the scene)")
done = False
while (not done):
    try:
        print(next(iterator)) # This is like calling iterator.__next__
    except StopIteration:
        done = True

print("\nCustom iterator implementation :\n")

# NEVER do this in Python : there are better ways with Generators: refere next chapter
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
