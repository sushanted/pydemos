
class Maximization:
    def __init__(self,capacity,weight_to_price_map,indent):
        self.capacity = capacity
        self.weight_to_price_map = weight_to_price_map
        self.indent = indent


def memoise(func):
    memoised_results = {}
    def memoised_decorator(capacity, weight_to_price_map, indent):
        pass
    return memoised_decorator;

# WIP above

def maximize(capacity, weight_to_price_map, indent):
    print(indent, capacity, weight_to_price_map)

    max_cost = 0
    max_cost_string = ""

    for weight, price in weight_to_price_map.items():
        remaining_capacity = capacity - weight
        if remaining_capacity >= 0:
            print(indent + "Used weight:", weight)

            cost, cost_string = maximize(  #
                remaining_capacity,  #
                dict([(nk, nv) for nk, nv in weight_to_price_map.items() if weight != nk]),  #
                indent + "\t"  #
            )
            cost = cost + price
            cost_string = cost_string + "+" + str(weight)

            if cost > max_cost:
                max_cost = cost
                max_cost_string = cost_string

    return max_cost, max_cost_string


print(maximize(20, {5: 2, 7: 8, 9: 10, 2: 7, 8: 9}, ""))
