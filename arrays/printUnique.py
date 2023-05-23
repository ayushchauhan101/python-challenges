# return unique value from the list

# # method 1
# def stray(arr):
#     for x in arr:
#         if arr.count(x) == 1:
#             return x

# method 2 ; return the element with the minimum count score i.e. 1
def stray(arr):
    return min(arr, key=arr.count)


print(stray([1,1,2,4,4,6,6]))
print(stray([2,2,3,2]))
print(stray([1, 1, 1, 1, 1, 1, 2]))
