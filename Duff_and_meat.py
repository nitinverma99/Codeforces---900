need = []
cost = []
sum = 0
for cases in range(int(input())):
    a, b = list(map(int, input().split()))
    need.append(a)
    cost.append(b)
minn = cost[0]
for i in range(len(need)):
    minn = min(minn, cost[i])
    sum +=  minn*need[i]
print(sum)