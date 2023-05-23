str = ''
n = 5

# for i in range(n):
#     str += ' '*(n-i)
#     str +=  '* '*i
#     str += '\n'

# print(str)


for i in range(n):
    str += ' '*(n-i)
    str += '*'*(2*i) + '*'
    str += '\n'

print(str)


# for i in range(n):
#     print(' '*(n-i), end='')
#     for j in range(i):
#         print(j, end=' ')
#     print('\n')

