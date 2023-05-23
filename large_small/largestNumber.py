check = 0

arr = [2,4,5,1,4,6,8,4,2,9,3]

# for i in range(len(arr)):
#     if arr[i] > check:
#         check = arr[i]
# print(check)

# print(max(arr))

def findLargest(num):
    low = 0
    for i in range(len(num)):
        if num[i] > low:
            low = num[i]
    return low


print(findLargest(arr))