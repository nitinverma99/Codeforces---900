for cases in range(int(input())):
    n, k = list(map(int, input().split()))
    if n%2 == 0:
        print(n + k*2)
    else:
        for i in range(3, n+1, 2):
            if n%i ==0:
                l = i
                break
        print( l + n + (k-1)*2)