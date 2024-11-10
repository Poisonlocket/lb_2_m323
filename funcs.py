from functools import reduce

def square(numbers):
    squared = list(map(lambda x: x ** 2, numbers))
    return squared

def eliminate_odd(numbers):
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    return evens

def sum(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total


# combine them all / put it on steroids
def all_of_them(numbers):
    result = reduce( lambda x, y: x + y,  # Step 3: reduce
    filter(
        lambda x: x > 10,  # Step 2: filter
        map(lambda x: x ** 2, numbers)  # Step 1: map
        )
    )
    return list(result)