for cases in range(int(input())):
    k = int(input())
    lst = list(map(int, input().split()))
    odd = []
    even = []
    for i in range(k):
        if lst[i]%2 == 0:
            even.append(lst[i])
        else:
            odd.append(lst[i])
    if len(odd) == k:
        print("YES")
    elif len(even) == k:
        print("YES")
    else:
        print("NO")