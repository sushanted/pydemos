import sys
from argparse import ArgumentParser

# Gives simple space separated args
print(sys.argv)

# argparse is more sophisticated parser
# General information about the module
parser = ArgumentParser(prog="demo", description="Demonstrate Command line parsing")
# Arg with no value
parser.add_argument("-flag", action="store_true")
# Type can be specified, default value for args can be specified
parser.add_argument("-n", type=int, default=10)
# By default type is str, aliases can be specified
parser.add_argument("-k", "-key", "--key", help="specify the value for the key")
parser.add_argument("--name")
# Unspecified args will have value as None
parser.add_argument("--unspecified")
# Multiple arguments
parser.add_argument("values", nargs="*")

parsed_arguments = parser.parse_args()

print(parsed_arguments)

# This prints the help about the command line
print("\n\nFollows the HELP:")
parser.print_help()
