for cases in range(int(input())):
    n ,a,b,c,d = list(map(int, input().split()))
    grain_min = n* (a-b)
    grain_max = n*(a+b)
    for i in range(c-d, c+d+1):
        if grain_min <= i <= grain_max:
            print("Yes")
            break
        elif i == c+d:
            print("No")
            break