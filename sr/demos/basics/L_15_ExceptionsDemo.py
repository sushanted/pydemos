# Simple exception handling
# Very similar to java try catch
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Zero division error occured")

# Getting exception object
try:
    x = 5 / 0
except ZeroDivisionError as z:
    print(z.args)

# Handling multiple errors/exceptions

for value in (0, "string", 6):
    try:
        x = 24 / value
        print(y)  # this is intended error
    except(NameError, ZeroDivisionError, TypeError, ValueError) as error:
        print("Error this time: ", error)


# Exception handling order and class hierarchy
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


print("derived to base progression")
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

print("base to derived progression")
for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")

print("\nHandle any exception and raise again:\n")
try:
    try:
        x = 5 / 0
    except:
        print("Some error occured, I don't care, let the caller take care")
        raise
except Exception as e:
    print(e)

print("\nElse clause : if exception doesn't occur\n")

for i in (0, 5):
    try:
        x = 5 / i
    except:
        print("Some error occured first")
    else:
        print("But now All is well!!")

print("\nException arguments\n")
try:
    # raising an exception
    raise Exception("Problem", 345)
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)
    string, number = e.args  # unpack
    print(f"{string} with {number}")

print("\nUser defined exceptions\n")


class MyException(Exception):
    def __init__(self, severity, message):
        self.severity = severity
        self.message = message

    def __str__(self):  # This is like toString in java
        return f"Exception occured with severity: {self.severity} , details: {self.message}"


try:
    raise MyException(4, "General message")
except MyException as mye:
    print("Caution: " + str(mye))

print("\nFinally clean-up\n")


def try_finally():
    value = 4
    try:
        return (value := value + 1)  # return expression is evaluated but not returned
    finally:
        return value  # Finally is finally returned instead of the one in 'try'


print("Finally returned:", try_finally())


def try_except_finally():
    try:
        x = 5 / 0
    except ZeroDivisionError:
        return "error"
    finally:
        return "finally"  # Finally is finally returned instead of the one in 'try'


print("Finally returned:", try_except_finally())

print("\nFinally finally runs!\n")


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("(except) division by zero!")
    else:
        print("(else) result is", result)
    finally:
        print("(finally) executing finally clause in any case!")


for (x, y) in [(2, 1), (2, 0), ("x", "y")]:
    try:
        print("Trying pair :", x, y)
        divide(x, y)
    except:
        pass  # intentional do nothing so program terminates normally
