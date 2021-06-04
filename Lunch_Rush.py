n, k = list(map(int, input().split()))
lst = []
for cases in range(n):
    a,b = list(map(int, input().split()))
    lst.append([a,b])
lst.sort(reverse = True, key = lambda x: x[0])
gst = []
for i in range(n):
    if lst[i][1] > k:
        gst.append(lst[i][0] - lst[i][1] + k)
    else:
        gst.append(lst[i][0])
print(max(gst))