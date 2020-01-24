import math, random, statistics

print(math.factorial(4))

print(math.log2(1024))

print("\nRandoms\n")

print("Random float number: ", random.random())

print("Random int number between 1-6 including 1 and 6: ", random.randint(1, 6))

# Same as above
print("Random in range: ", random.randrange(1, 6))

print("Random element from a sequence: ", random.choice('some character'))

print("Random numbers from 1 to 10, without replacement: no repeat", random.sample(range(10), 10))

print("Random character from string, without replacement: no repeat (index)", random.sample('the_unique_sample', 10))

print("\nStatistics\n")

data = [1, 3, 4, 1, 4, 7, 4, 7, 7, 8, 9, 0, 3, 9, 9, 9]

print("Data: ", sorted(data))

print("Mean:", statistics.mean(data))

print("Median:", statistics.median(data))

print("Mode:", statistics.mode(data))

print("Variance:", statistics.variance(data))

print("Standard Deviation:", statistics.stdev(data))
