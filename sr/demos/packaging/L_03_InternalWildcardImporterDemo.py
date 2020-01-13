# NOT A GOOD PRACTICE DUE TO POSSIBLE NAME COLLISION AND POLLUTION

from sr.demos.packaging.lib import *

# Can use the names directly, they become part of this(importer) symbol table
print(multiples(4))
print(factors(122))

print(is_prime(8))
print(number_of_multiples)

# Not imported (by import *) because the name starts with _ , can be imported explicitly
#print(_multiple_start_range)