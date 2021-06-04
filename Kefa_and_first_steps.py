n = int(input())
lst = list(map(int, input().split()))
count = 1
maxx = 1
for i in range(n-1):
    if lst[i] <= lst[i+1]:
        count += 1
    else:
        if count>maxx :
            maxx = count
        count = 1
if count > maxx:
    print(count)
else:
    print(maxx)
