# # append() ; the original list is changed 
# currencies = ['Dollar', 'Euro', 'Pound']
# currencies.append('Yen')
# print(currencies)

# list1 = [1,2,3]
# list2 = [6,7,8]

# list1.append(list2)
# list1.append(10)
# print(list1)


# ----------------------------
# # extends()
# list1 = [1,2,3]
# list2 = [6,7,8]

# # list1.extend(list2)
# # print(list1)

# # same result:
# list1 += list2
# print(list1)


# ----------------------------
# # index('character', start, end)
# vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# print(vowels.index('u'))
# print(vowels.index('i'))


# ----------------------------
# # insert(index,'element')
# mixed_list = [{1, 2}, [5, 6, 7]]
# mixed_list.insert(1,(4,5))
# print(mixed_list)


# ----------------------------
# # count
# numbers = [2, 3, 5, 2, 11, 2, 7]
# count = numbers.count(2)
# print('Count of 2:', count)


# ----------------------------
# pop(index)
# prime_numbers = [2, 3, 5, 7]
# removedElement = prime_numbers.pop(1)
# print(f'the popped item is: {removedElement} and the updated list is: {prime_numbers}')
# print(prime_numbers.pop(-2))


# ----------------------------
# reverse() ; changes the existing list
# nums = [2, 3, 5, 7]
# # print(nums[::-1]) #same output using slicing
# nums.reverse()
# print(nums)

# systems = ['Windows', 'macOS', 'Linux']

# for x in reversed(systems):
#     print(x, end=' ')


# ----------------------------
# sort(key=,reverse=True/False)
# nums = [4,2,7,2,9,1]
# nums.sort(reverse=True)
# print(nums)

# Note: The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't return any value, while sorted() doesn't change the list and returns the sorted list.

# print(sorted(nums))

# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# print(sorted(random))

# def secondElem(arr):
#     # returning second element
#     return arr[1]

# # sorting by second element
# random.sort(key=secondElem)
# print(random)

employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# # .get to call value in a set {}
# # assinging employees to arr and returning age
# def sortByAge(arr):
#     return arr.get('age')

# employees.sort(key=sortByAge)
# print(employees)


# employees.sort(key=lambda arr: arr.get('salary'))
# print(employees)

# sorted(list, key=len)
# print(sorted(employees, key=lambda arr: arr.get('Name')))

