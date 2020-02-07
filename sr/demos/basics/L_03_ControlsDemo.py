# if else if
number = int(input("Enter number:"))
if number == 1:
    print("one")
elif number == 2:
    print("two")
else:
    print("more than two")

# Ternary operator equivalent statement : number % 2 == 1 ? "odd":"even"

number_type = "odd" if number % 2 == 1 else "even"
print("The entered number is: ", number_type)

# for
for c in "word":
    print(c)

# from 0 till n excluding n
for i in range(3):
    print("till 3:", i)

for i in range(3, 7):
    print("3 till 7:", i)

for i in range(0, 10, 2):
    print("even number:", i)

# Note: range gives an iterable (NOT a list)
print("Sum of first 5 natural numbers", sum(range(1, 6)))

print("First 5 numbers", list(range(5)))

print("Break and Else for 'for'")

# "else" clause will be executed only if the loop completes normally (without a break)
#  a loops else clause runs when no break occurs
for i in range(1, 7):
    print("visited", i)
else:
    print("All numbers in the range visited, last number visited: ")

# classic example:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for i in range(1, 7):
    print("visited", i)
    if i == 2: break
else:
    print("This will not be printed, as some numbers not visited")

print("\n else for while \n")
i = 10
while (i < 10):
    i = i + 1
else:
    print("i >= 10")

for i in range(0, 10):
    if (i % 3 == 0):
        continue;
    print("Number not divisible by 3 :", i)

# Python needs this because it is indentation based : effectively it is empty curly braces
for i in range(1, 4):
    pass


# Another example of else of a for loop (Needs a forward reference of Functions chapter):
def factorize(number):
    print("Computing factors of:", number)
    for factor in range(2, (number // 2) + 2):
        if number % factor == 0:
            return [factor] + factorize(number // factor)
    else:
        if number == 1:
            return []
        # No factor could break the number, i.e. it is the prime number
        return [number]


print("Factors of 16:", factorize(16))
