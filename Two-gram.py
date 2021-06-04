n = int(input())
s = input()
gst = []
for i in range(n-1):
    s1 = s[i:i+2]
    gst.append(s1)
print(max(gst, key=gst.count))