# import function using the same name as in imported module
from sr.demos.packaging.lib import factors
# import variable
from sr.demos.packaging.lib import  _multiple_start_range
# import function using a new name
from sr.demos.packaging.lib import multiples as table

# Multiple imports in a single statement
from math import factorial,log2 as log

# Can use the names directly, they become part of this(importer) symbol table
print(factors(122))
# factors is imported with a different name, useful to avoid name collision or simplification
print(table(4))

# Can be imported explicitly but not through import *
print(_multiple_start_range)

# not accessible as they are not imported
#print(is_prime(8))
#print(number_of_multiples)

print(log(256))
print(factorial(4))