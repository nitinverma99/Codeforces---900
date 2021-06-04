for cases in range(int(input())):
    n = int(input())
    remain = n%2020
    k = (n-remain)/2020
    x = k - remain
    if x>= 0:
        print("YES")
    else:
        print("NO")