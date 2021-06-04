for cases in range(int(input())):
    n,x = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    minn = sum(lst)
    if minn%x==0:
        minn = minn//x
    else:
        minn = minn//x + 1

    maxx = 0
    for i in range(n):
        if lst[i]%x == 0:
            maxx += lst[i]//x
        else:
            maxx += (lst[i]//x) + 1
    print(minn, maxx)