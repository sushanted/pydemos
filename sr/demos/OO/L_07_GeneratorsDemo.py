from datetime import datetime

print("\nGenerator:\n")


def single_value_generator():
    hour_of_the_day = datetime.now().hour;
    if hour_of_the_day < 12:
        yield "Good morning!"
    elif hour_of_the_day >= 12 and hour_of_the_day < 17:
        yield "Good afternoon!"
    elif hour_of_the_day >= 17 and hour_of_the_day < 21:
        yield "Good evening!"
    elif hour_of_the_day >= 21:
        yield "Good night!"


svg = single_value_generator()
print("Single value generated: ", next(svg))

try:
    print(next(svg))
except StopIteration:
    print("No more values!")


# Method of working (from the python tutorial):

# 1. A generator is called like a function. Its return value is an iterator, i.e. a generator object.
#    The code of the generator will not be executed at this stage.
# 2. The iterator can be used by calling the next method. The first time the execution starts like a function,
#    i.e. the first line of code within the body of the iterator. The code is executed until a yield statement is reached.
# 3. yield returns the value of the expression, which is following the keyword yield. This is like a function,
#    but Python keeps track of the position of this yield and the state of the local variables is stored for the next call.
#    At the next call, the execution continues with the statement following the yield statement and the variables have the
#    same values as they had in the previous call.
# 4. The iterator is finished, if the generator body is completely worked through or if the program flow encounters a return
#    statement without a value.

def multi_value_generator():
    yield "Monday"
    yield "Tuesday"
    yield "Wednesday"
    yield "Thursday"
    yield "Friday"


for day in multi_value_generator():
    print(day)


# With generators there is no need to write iterators methods : __next__ , no need to maintain interim state,
# and no need to check the end of iteration and raise StopIteration
def reverse_squares():
    for i in range(10, 0, -1):
        # yield should always be in a function
        yield i * i


print("Reversed squares")
for i in reverse_squares():
    print(i)


# Same example as that of iterator (without state maintenance), yield can be done at any point in the function
def squares(upto):
    last_square_number = 0
    current_difference = 1
    while (last_square_number + current_difference) < upto:
        last_square_number = last_square_number + current_difference
        yield last_square_number
        current_difference = current_difference + 2


print("Squares upto 101")
for i in squares(101):
    print(i)

print("\nReturn in generator:\n")


def returning_generator():
    yield "Normal value"
    # This is equivalent to : raise StopIteration("Generator Finished")
    return "Generator Finished"


rg = returning_generator()
print(next(rg))
try:
    print(next(rg))
except StopIteration as si:
    print("Stop iteration args: ", si.args)

print("\nSending message back to a generator:\n")


# NOTE : next(gen) and gen.send(value) both send and receive value from the generator (first send and then receive)
#        next(gen) SENDS None to the generator while receives the next yielded value
#        gen.send(value) sends the provided value to the generator while receives next yielded value

# Summary : The function execution halts after the RHS part of the yield is evaluated, LHS assignment happens after another next or send call
# The value sent by the send is actually used for next yield, i.e. return value of the send is product of the sent value
# Details:
# one next() needs to be called to start the generator : execute first statement in the generator
# send() cannot be done on a generator which has not been started (at-least one next() needs to be called on the generator before calling the send)
# calling the next() on generator first time, executes the statements upto first yield statement, the yield value is returned to called of the next()
# the assignment at the yield waits till next() or send() is called
# if next is called : None is assigned to the LHS variable in previous yeild statement and the execution proceeds till another yield is encountered
# if send is called : the sent value is assigned to the LHS variable in previous yield statement and the execution proceeds till another yield is encountered


def simple_listening_generator(value):
    print("starting the generator, first 'next' got called, starting value provided to the generator as arg is: ",
          value)
    while True:
        print("value being yielded: ", value, " ,after yielding we will wait for a 'next' or 'send'")
        value = yield value
        print("\n wait over")
        if value:
            print("'send' sent value: ", value, " ,this value will be used to yield next value.")
        else:
            print("seems 'next' got called")


slg = simple_listening_generator(1)
# Generator needs to be started (at-least one next() to be called on it), before sending any value to it
# Following statement will throw an Exception
# slg.send(2)
print("Yielded value by 'next':", next(slg))
# Now the generator is started, values can be sent to it
print("Yielded value by 'next':", next(slg))
print("Yielded value by 'send':", slg.send(2))
print("Yielded value by 'next':", next(slg))
print("Yielded value by 'send':", slg.send(5))

print("\n\n")


def listening_generator():
    value = 1
    while value < 10:
        print("Next value for yielding: ", value)
        skip_values = yield value
        print("skip_values: ", skip_values)
        if skip_values:
            value = value + skip_values
        else:
            value += 1


lg = listening_generator()
for i in lg:
    print("Generated value: ", i)
    if i == 3:
        print("Skipping next 2 values")
        print("Generated value: ", lg.send(2))

print("\nThrow onto a generator")


# This could be a way to signal a stop an infinite generator (and make any cleanup)
# Note : throw also returns the next yielded value

def catching_generator():
    exception_thrown = False
    for i in range(1, 11):
        try:
            yield i
            if exception_thrown:
                break
        except Exception:
            exception_thrown = True
            print("Exception thrown by the user, will still generate a next value and then will end!")


cg = catching_generator()

for i in cg:
    print("Yielded value:", i)
    if i == 4:
        print("Yielded value after throwing:", cg.throw(Exception))

print("\nYield from: ")


# Yield from can be used for any iterable

def recursive_infinite_generator():
    yield from "0123456789"
    # After above sequence is exhausted, yielding will start with next yield from
    yield from recursive_infinite_generator()


rg = recursive_infinite_generator()
for i in range(20):
    print("Next: ", next(rg))


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


# Interesting Examples:

print("\nBFS generator:")


def bfs_generator(value):
    level = 0
    next_values = [value, None]
    while True:
        popped_value = next_values.pop(0)
        if not popped_value:
            level += 1
            next_values.append(None)
            continue
        yield level,popped_value
        next_values.extend([popped_value - 1, popped_value + 1])


bg = bfs_generator(7)
for i in range(15):
    print(next(bg))