import sr.demos.packaging.lib as lib

# only lib is imported into symbol table of this importer, symbols from the imported module need to be accessed
# using the import name (lib in this case)

print("Using library: ", lib.__name__)

# Access functions in other packaging
print(lib.multiples(4))
print(lib.factors(49))
print(lib.is_prime(7))
print(lib.is_prime(8))

# Access variables in other packaging
lib.number_of_multiples = 4
# Can access names starting with _ as well
print(lib._multiple_start_range)

print(lib.multiples(6))

print("Calling module:",__name__)
lib.print_module_name()

