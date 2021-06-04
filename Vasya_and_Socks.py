n,m = list(map(int, input().split()))
cnt= n
while(n>=m):
    cnt += n//m
    n = n//m + n%m
print(cnt)