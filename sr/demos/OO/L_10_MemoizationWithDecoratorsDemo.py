# Revisit this after OOPs chapter, it needs some references

class MaximizationData:
    def __init__(self, capacity, weight_to_price_map, indent):
        self.capacity = capacity
        self.weight_to_price_map = weight_to_price_map
        self.indent = indent

    def __str__(self):
        return str(self.indent) + str(self.capacity) + " " + str(self.weight_to_price_map)

    def __hash__(self):
        hash = self.capacity * 31
        for weight in sorted(self.weight_to_price_map.keys()):
            hash = hash * 31 + weight
        return hash

    def __eq__(self, other):
        return \
            self.capacity == other.capacity and \
            sorted(self.weight_to_price_map.keys()) == sorted(other.weight_to_price_map.keys())

# WIP below

class Memoiser:
    def __init__(self,func):
        self.memoised_results = {}
        self.func = func

    def __call__(self,maximization_data):
        if (maximization_data in self.memoised_results):
            print(f"Found memoised result for {str(maximization_data)} : {self.memoised_results[maximization_data]}")
            return self.memoised_results[maximization_data]
        result = self.func(maximization_data)
        self.memoised_results[maximization_data] = result
        return result
        pass

# WIP above

def memoise(func):
    memoised_results = {}

    def memoised_decorator(maximization_data):
        if (maximization_data in memoised_results):
            print(f"Found memoised result for {str(maximization_data)} : {memoised_results[maximization_data]}")
            return memoised_results[maximization_data]
        result = func(maximization_data)
        memoised_results[maximization_data] = result
        # print(memoised_results)
        return result

    return memoised_decorator;



@memoise
def maximize(maximization_data):
    print(str(maximization_data))

    max_cost = 0
    max_cost_string = ""

    for weight, price in maximization_data.weight_to_price_map.items():
        remaining_capacity = maximization_data.capacity - weight
        if remaining_capacity >= 0:
            print(maximization_data.indent + "Used weight:", weight)

            cost, cost_string = maximize(  \
                MaximizationData(  \
                    remaining_capacity,  \
                    dict([(nk, nv) for nk, nv in maximization_data.weight_to_price_map.items() if weight != nk]),  \
                    maximization_data.indent + "\t"  \
                )  \
            )
            cost = cost + price
            cost_string = cost_string + "+" + str(weight)

            if cost > max_cost:
                max_cost = cost
                max_cost_string = cost_string

    return max_cost, max_cost_string


print(maximize(MaximizationData(20, {5: 2, 7: 8, 9: 10, 2: 7, 8: 9}, "")))


