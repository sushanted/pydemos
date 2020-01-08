print("\nLambdas\n")


# Precursor
def adder(a, b):
    return a + b


def adder_factory():
    return adder


print("addition:", adder_factory()(3, 4))


def adder_lambda_factory():
    return lambda a, b: a + b


print("addition:", adder_lambda_factory()(3, 4))

# lambda assignment
printer = lambda a: print(a)
printer("hello")


# value of x is bound into lambda being returned
def make_incrementer(x):
    return lambda y: x + y


incr = make_incrementer(5)
print(incr(2))
print(incr(3))


# passing the lambda to a function
def calculator(a, b, fun):
    return fun(a, b)


print(calculator(3, 4, lambda x, y: x + y))
print(calculator(3, 4, lambda x, y: x * y))
print(calculator(3, 4, lambda x, y: x - y))


# lambda accepting lambda : fun is lambda
def create_calculator(x, y):
    return lambda fun: fun(x, y)


calculator = create_calculator(7, 2)
print(calculator(lambda a, b: a + b))
print(calculator(lambda a, b: a * b))
print(calculator(lambda a, b: a - b))
# any function can also be passed by name
print(calculator(adder))
