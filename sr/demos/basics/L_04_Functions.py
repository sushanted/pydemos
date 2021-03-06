# definition
def fun(x, y):
    print(x + y)


# call
fun(3, 4)

# function can be references by its name and can be assigned to another variable
new_fun = fun
new_fun(4, 5)

print("\nDefault arguments\n")


def fun_default(number, multiple=1, msg='Multiplication'):
    print((msg, number * multiple))


# defaulting
fun_default(3)
fun_default(3, 5)
fun_default(3, 6, "product")


# mutable default values would mutate with each mutating call and will be used in later calls
def fun_default_mutable(x, list=[]):
    list.append(x)
    print("after append", list)


fun_default_mutable(1)
fun_default_mutable(2)
fun_default_mutable(3)
fun_default_mutable(4, [])  # new list provided
fun_default_mutable(5)  # continue using default list

print("\nKeyword parameters\n")
fun_default(6, msg="product")
# position can be altered while calling, provided proper name is given
fun_default(7, msg="product", multiple=7)

fun_default(msg="product", number=9)
# keyword arguments must follow positional arguments, following won't work
# fun_Default(msg="product",4)

# Special parameters

print("\nPosition only\n")


def position_only(a, b, /):
    print(a, b)


print("\nKeywords only\n")


def keyword_only(*, a, b):
    print(a, b)


print("\nMixed\n")


def mixed(posonly1, posonly2, /, standard1, standard2, *, keyword_only1, keyword_only2):
    print(posonly1, posonly2, standard1, standard2, keyword_only1, keyword_only2)


position_only(5, 6)
keyword_only(b=4, a=5)
mixed(2, 3, 2, standard2=4, keyword_only1=0, keyword_only2=9)


# Arbitrary arguments : args after var-arg can only be keyword args, as var-arg eats up all the parameters passed
def concat(*parts, sep="/"):
    return sep.join(parts)


print(concat("a", "b", "c"))
print(concat("10", "100", "23", "56", sep="."))


def consume_keyword_args(non_keyword, **dictionary):
    print("non_keyword:", non_keyword)
    print("dictionary:", dictionary)


# Pass key value pairs, all not matching params are passed to the dictionary arg
consume_keyword_args(a=1, b=2, non_keyword=10, c=3)

print("\nFunction namespace and inner instances:\n")


def outer(value):
    # For every call for the outer function a new inner function is defined
    def inner():
        pass

    # Values can be defined in the namespace of the function
    # This value would be different for each returned function reference
    inner.value = value
    return inner


first_call_result = outer(1)
second_call_result = outer(2)

# Every time a new instance of inner function is returned
print(id(first_call_result), id(second_call_result))
print("Are the inner functions same? ", first_call_result == second_call_result)
print(first_call_result.value, second_call_result.value)
