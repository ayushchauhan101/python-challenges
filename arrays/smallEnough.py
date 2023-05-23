# You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value.

# method 1
# def small_enough(array, limit):
#     for x in array:
#         if (x > limit):
#             return False
#     return True


# method 2
def small_enough(array,limit):
    return max(array) <= limit


print(small_enough([78, 117, 110, 99, 104, 117, 107, 115] ,100))
print(small_enough([80, 117, 115, 104, 45, 85, 112, 115] ,120))