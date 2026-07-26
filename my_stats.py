import math

def mean(numbers):
    return sum(numbers) / len(numbers)

def variance(numbers):
    avg = mean(numbers)
    total = 0

    for num in numbers:
        total += (num - avg) ** 2

    return total / len(numbers)

def std_deviation(numbers):
    return math.sqrt(variance(numbers))