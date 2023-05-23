# method 1
# def quarter_of(month):
#     if 1 <= month <= 3:
#         return 1
#     if 4 <= month <= 6:
#         return 2
#     if 7 <= month <= 9:
#         return 3
#     if 10 <= month <= 12:
#         return 4

# method 2 
# import math

# def quarter_of(month):
#     return math.ceil(month/3)


# method 3
# The floor division operator // rounds the result down to the nearest whole number
def quarter_of(month):
    return (month + 2) // 3

print(quarter_of(2))
print(quarter_of(8))
print(quarter_of(10))