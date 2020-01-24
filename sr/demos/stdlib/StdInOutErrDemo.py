import sys

print("Enter some text:")
print("Input:", sys.stdin.readline())
sys.stdout.write("Standard out")
sys.stderr.write("Standard error")

# Another mechanism to take input
i = int(input("Input a number:"))
print(f"Square if {i} = {i * i}")
