for cases in range(int(input())):
    n = int(input())
    lst= list(map(int, input().split()))
    condition = (n*n - n - 2)//2
    value =True
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            pass
        else:
            value=False
            break

    if value:
        print("NO")
    else:
        print("YES")
     


