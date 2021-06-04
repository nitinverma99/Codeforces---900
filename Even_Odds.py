n, k = list(map(int, input().split()))
if k<= (n+1)//2 :
    print(int(2*k-1))
else:
    print(int((k-(n+1)//2)*2))