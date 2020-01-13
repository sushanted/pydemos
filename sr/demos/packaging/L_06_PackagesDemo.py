# import a specific module from a package
from sr.demos.packaging import lib

# import a package
import sr.demos as demo_package
import sr.demos.packaging as imported_package

# Following won't work, the last item must be a package or a module (And not a variable,function or a class)
# import sr.demos.packaging.lib.factors

# use imported module
print(lib.factors(45))

# use imported package to reference inner modules
demo_package.packaging.lib.print_module_name()

# calling package level method defined in __init__.py of the imported package
# __init__.py represents the package
imported_package.module_level_method()