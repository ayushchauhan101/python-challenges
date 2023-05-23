nums = [1,2,3,4,2]
mySet = set()

for n in nums:
    # check for duplicate
    if n in mySet:
        print(f'duplicate found : {n}')
    # if not present already, add element to mySet
    else:
        mySet.add(n)
        print(f'no duplicate of {n} found!')