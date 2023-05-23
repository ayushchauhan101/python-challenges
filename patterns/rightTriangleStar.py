n = 5

for i in range(n):
    print(' '*(n-i) + '*'*i)

for i in range(n):
    print(' '*(n-i), end='')
    for j in range(i):
        print('*', end='')
    print('\n')

