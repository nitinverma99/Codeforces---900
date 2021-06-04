n = int(input())
lst = list(map(int, input().split()))
even = 0
for i in range(n):
    if lst[i]%2 ==0 :
        even += 1
print(min(even, n-even))