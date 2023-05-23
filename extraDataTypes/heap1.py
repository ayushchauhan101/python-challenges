import heapq

arr = [2,3,5,7,1,4,9,8]
print(arr)

heapq.heapify(arr)
print(arr)

print(heapq.nsmallest(arr,0))
print(heapq.nsmallest(arr,1))

