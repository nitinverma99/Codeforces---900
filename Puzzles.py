n,m = list(map(int, input().split()))
lst = list(map(int, input().split()))

gst = []
if n==m and n==2:
    print(abs(lst[1]-lst[0]))
else:
    lst.sort()
    for i in range(len(lst)-n+1):
        gst.append(lst[i+n-1] - lst[i])
    print(min(gst))