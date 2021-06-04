n = int(input())
lst = list(map(int, input().split()))
minn = lst[0]
maxx = lst[len(lst)-1]
value1, value2 = 0, 0
for i in range(len(lst)):
    if i ==0 :
        print(abs(lst[1]-lst[0]),abs(maxx-minn))
    elif i == len(lst)-1 :
        print(abs(lst[len(lst)-1]-lst[len(lst)-2]),abs(maxx-minn))
    else:
        if abs(lst[i]- lst[i-1]) > abs(lst[i+1]-lst[i]):
            value1 = abs(lst[i+1]-lst[i])
        else:
            value1 = abs(lst[i]- lst[i-1])
        if abs(lst[len(lst)-1] - lst[i]) > abs(lst[0] - lst[i]):
            value2 = abs(lst[len(lst)-1] - lst[i])
        else:
            value2 = abs(lst[0] - lst[i])
        print(value1, value2)