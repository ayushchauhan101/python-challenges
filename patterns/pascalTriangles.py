n = 5

res = [[1]]

for i in range(n-1):
    temp = [0] + res[-1] + [0]
    row = []
    for j in range(len(res[-1]) + 1):
        row.append(temp[j] + temp[j+1])
