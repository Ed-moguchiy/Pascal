N = int(input())
T = []
for i in range (N):
    row = [1] * (i+1)
    for j in range (i+1):
        if j != 0 and j != i:
            row[j] = T[i-1][j-1]+T[i-1][j]
    T.append(row)            

for k in range(len(T)):
    print (' ' * (N - k), end = '')
    print(*T[k])
