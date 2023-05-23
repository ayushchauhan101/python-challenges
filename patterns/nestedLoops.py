n = 5
word = 'ayush chauhan'
# print(len(word))

# for i in range(n):
#     print(' '*(n-i), end='')
#     for j in range(i):
#         print(j, end=' ')
#     print('\n')

# for i in range(len(word)):
#     for j in range(i+1):
#         print(word[j], end='')
#     print('\n')


for i in range(1,n+1):
    for j in range(i):
        print('*', end='')
    print('\n')