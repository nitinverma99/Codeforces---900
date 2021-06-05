for cases in range(int(input())):
    n,a,b = list(map(int, input().split()))
    s = 'abcdefghijklmnopqrstuvwxyz'
    call = s[:b] * 2000
    print(call[:n])
