# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.
# Square all numbers k (0 <= k <= n) between 0 and n.
# Count the numbers of digits d used in the writing of all the k**2. 

# def nb_dig(n, d):
#     square = []
#     for i in range(n+1):
#         square.append(i**2)
#     return square



# print(nb_dig(10,9))

# arr = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# count_arr = ' '.join(map(str, arr))
# print(count_arr.split(' '))

# count = 0
# for x in arr:
#     if x == 9:
#         count += 1
#     elif len(x) == 2:
#         print(x)

# print(count)

nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(x+2 for x in nums)