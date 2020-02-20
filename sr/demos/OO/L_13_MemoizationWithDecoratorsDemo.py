# Revisit this after OOPs chapter, it needs some references

# This is very generic memoiser now, this can be used generically for any DP problem
# User just need to define the optimizer_function and memoisable_data
class Memoiser:
    def __init__(self, optimizer_function):
        self.memoised_results = {}
        self.optimizer_function = optimizer_function

    def __call__(self, memoisable_data):
        if (memoisable_data in self.memoised_results):
            print(f"Found memoised result for {str(memoisable_data)} : {self.memoised_results[memoisable_data]}")
            return self.memoised_results[memoisable_data]
        # This will call the actual function,
        # but remember the recursive calls from actual function will call the decorated function
        result = self.optimizer_function(memoisable_data)
        self.memoised_results[memoisable_data] = result
        return result

# Use-case 1 : Cost maximization

class MaximizationData:
    def __init__(self, capacity, weight_to_price_map, indent):
        self.capacity = capacity
        self.weight_to_price_map = weight_to_price_map
        self.indent = indent

    def __str__(self):
        return str(self.indent) + str(self.capacity) + " " + str(self.weight_to_price_map)

    # TODO think of optimizing following two methods, the sorting and comparisions look heavy
    def __hash__(self):
        hash_value = self.capacity * 31
        for weight in sorted(self.weight_to_price_map.keys()):
            hash_value = hash_value * 31 + weight
        return hash_value

    def __eq__(self, other):
        return \
            self.capacity == other.capacity and \
            sorted(self.weight_to_price_map.keys()) == sorted(other.weight_to_price_map.keys())


@Memoiser
def maximize(maximization_data):
    print(str(maximization_data))

    max_cost = 0
    max_cost_string = ""

    for weight, price in maximization_data.weight_to_price_map.items():
        remaining_capacity = maximization_data.capacity - weight
        if remaining_capacity >= 0:
            print(maximization_data.indent + "Used weight:", weight)

            # This recursive call will call the decorated maximize function
            cost, cost_string = maximize( \
                MaximizationData( \
                    remaining_capacity, \
                    dict([(nk, nv) for nk, nv in maximization_data.weight_to_price_map.items() if weight != nk]), \
                    maximization_data.indent + "\t" \
                    ) \
                )
            cost = cost + price
            cost_string = cost_string + "+" + str(weight)

            if cost > max_cost:
                max_cost = cost
                max_cost_string = cost_string

    return max_cost, max_cost_string


print(maximize(MaximizationData(20, {5: 2, 7: 8, 9: 10, 2: 7, 8: 9}, "")))

# Use-case 2 : Fibonacci

# Re-using the same memoiser for different problem
@Memoiser
def n_th_fib(n):
    print("calculating fibonacci number at : ", n)
    # 0 1 1 2 3 5 8 13 21
    # 0 1 2 3 4 5 6  7  8
    if n < 2:
        return n
    return n_th_fib(n - 1) + n_th_fib(n - 2)


print("0th fibonacci number: ", n_th_fib(0))

print("1st fibonacci number: ", n_th_fib(1))

print("5th fibonacci number: ", n_th_fib(5))

# Note that same memoiser is getting used for all calls
# Following call will use memoised 5th fibonacci
print("50th fibonacci number: ", n_th_fib(50))
