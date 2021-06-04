n,m = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst.sort()
count = 0
for i in range(m):
    if lst[i] <= 0:
        count += lst[i]
    else:
        break
print(abs(count))