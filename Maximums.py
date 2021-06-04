n = int(input())
lst = list(map(int, input().split()))
gst = []
gst.append(lst[0])
x = gst[0]
for i in range(1, len(lst)):
        gst.append(lst[i]+x)
        x = max([x, gst[i]])
print(*gst)