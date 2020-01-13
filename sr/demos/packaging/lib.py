# This will get executed on running this file or even importing this lib
print("Library got imported or ran")

def print_module_name():
    print("Called Module:",__name__)

# __name__ is set as __main__ if it is the file which is run (and not imported)
if __name__ =="__main__":
    print("Library got ran, importing will not print this")
    # This will be __main__ if this file is run as script, otherwise it will be sr.demos.packaging.lib
    print_module_name()

_multiple_start_range = 1

number_of_multiples = 10

def multiples(number):
    return [number*i for i in range(_multiple_start_range,number_of_multiples+1)]

def factors(number):
    return [i for i in range(2,(number//2)+1) if number%i==0]

def is_prime(number):
    return number>1 and not factors(number)


