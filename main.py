spisok = list(map(int, input().split()))
for i in range(len (spisok)):
    for j in range(i, len(spisok)):
        if spisok[j] < spisok[i]:
            min = spisok[j]
            spisok[i], spisok[j] = min, spisok[i]
print (*spisok)    

print('kek') 

  