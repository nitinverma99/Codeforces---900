n = int(input())
lst = list(map(int, input().split()))
odd = []
even = []
summ = 0
zeroes = 0
for i in range(len(lst)):
    if lst[i] <= -1 :
        odd.append(lst[i])
    elif lst[i] >=1 :
        even.append(lst[i])
    else:
        zeroes += 1

for i in range(len(odd)):
    odd[i] = abs(odd[i] + 1)

for i in range(len(even)):
    even[i] -= 1

if len(odd)%2 != 0:
    if zeroes > 0:
        pass
    else:
        summ += 2

odd_sum = sum(odd)
even_sum = sum(even)
zeroes_sum = zeroes * 1
print(odd_sum + even_sum + zeroes_sum + summ)