n = 5

# method 1
# myList = list(x for x in range(1,n+1))
# myList.reverse()
# print(myList)

# method 2
print(list(range(n,0,-1)))


# method 3
print(list(x for x in range(n,0,-1)))