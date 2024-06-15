lst= list(map(int, input().split()))
n = len(lst)
for i in range(n):
    
    for j in range(0,n-1-i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            lstj = lst[j]
            lsti = lst[i]
            max = lst[j]






for i in range(0, n):
    for j in range(i,n-1-i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            lstj = lst[j]
            lsti = lst[i]
            max = lst[j]