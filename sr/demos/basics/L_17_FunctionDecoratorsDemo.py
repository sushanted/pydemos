import time, datetime


# takes input as a function and returns a decorator function
# func is function to be decorated
def log_decorator(func):
    # decorating function, calls actual function with input and returns the value returned by the actual function
    def decorate_log(x):
        print("calling func")
        returned_value = func(x)
        print("called func")
        return returned_value

    return decorate_log


print("\nDynamic decoration:\n")


def square(number):
    return number * number


print("simple call: ", square(3))
decorated_square = log_decorator(square)
print("decorated call: ", decorated_square(3))

print("\nStatic decoration:\n")

# The equivalent dynamic syntax is
# cube = log_decorator(cube)
@log_decorator  # this will apply the decoration for each invocation of the function
def cube(number):
    return number ** 3


# Here onwards cube is not cube but a decorated cube; cube() calls decorated cube; cube.x is the decorated cubes value

print("Statically decorated call: ", cube(4))

print("Decorated cube name:", cube.__name__)

print("\nA generic decorator:\n")


def generic_time_decorator(func):
    def decorate_with_time(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"time taken by {func.__name__}: {time.time() - start}")

    return decorate_with_time


# decorate one arg function
@generic_time_decorator
def printer(items):
    for i in items:
        time.sleep(1)
        print(i)


# decorate no arg method
@generic_time_decorator
def simple():
    pass


@generic_time_decorator
def mixed(a, b, **kwargs):
    print(a, b, kwargs)


printer([2, 3, 4])
simple()
mixed(3, 4, name='a')

print("\nDecorator with context:\n")


def count_decorator(func):
    # This function will be defined for each decoration call (whenever the outer function is called)
    # So each caller will get a different instance of the inner function as return value
    def decorate_with_count(*args, **kwargs):
        decorate_with_count.count += 1
        func(*args, **kwargs)

    # Note : we can put variables in the functions namespace as well
    decorate_with_count.count = 0
    # Each return will give a new instance of the inner function
    return decorate_with_count


@count_decorator
def one():
    pass


@count_decorator
def two():
    pass


for i in range(10):
    one()

for i in range(5):
    two()

print(f"one got called {one.count} times")
print(f"two got called {two.count} times")

print("\nDecorators with parameters:\n")


def log_time_decorator(log_time):
    def decorate_log_with_time(func):
        def _decorate_log_with_time(*args, **kwargs):
            print((str(datetime.datetime.now()) if log_time else "") + " calling: " + func.__name__)
            returned_value = func(*args, **kwargs)
            print((str(datetime.datetime.now()) if log_time else "") + " called: " + func.__name__)
            return returned_value

        return _decorate_log_with_time

    return decorate_log_with_time


print("Static Parameterized Decorations:")
print("Calling with log_time enabled:")
print(log_time_decorator(True)(square)(5))
print("Calling with log_time disabled:")
print(log_time_decorator(False)(square)(5))

print("Dynamic Parameterized Decorations:")

# Consider this as a call made to obtain the decorator which can accept a function
# double = log_time_decorator(True)(double)
@log_time_decorator(True)
def double(value):
    return 2 * value


print(double(10))
