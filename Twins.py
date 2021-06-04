n = int(input())
lst = list(map(int, input().split()))
i=0
count = 0
remain = sum(lst)
for i in range(n):
    maxx = max(lst)
    count += maxx
    remain = sum(lst) - maxx
    i+=1
    lst.remove(maxx)
    if count > remain:
        print(i)
        break
    else:
        continue