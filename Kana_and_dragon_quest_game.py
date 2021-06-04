for cases in range(int(input())):
    x, n ,m = list(map(int, input().split()))
    for i in range(n):
        if x>= 12:
            x = ((x//2) + 10)
        else:
            continue
    for i in range(m):
        x -= 10
    if x <= 0:
        print("YES")
    else:
        print("NO")