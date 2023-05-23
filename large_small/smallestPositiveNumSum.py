# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# method 1
# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     return numbers[0] + numbers[1]

# method 2
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])

# method 3
# from heapq import nsmallest

# def sum_two_smallest_numbers(numbers):
#     return sum(nsmallest(2,numbers))


# method 4
# using set to remove repeat numbers
def sum_two_smallest_numbers(numbers):
    mySet = set(numbers)
    myList = sorted(list(mySet))
    return myList[0] + myList[1]

print(sum_two_smallest_numbers([19, 5, 42, 2, 77,2]))
