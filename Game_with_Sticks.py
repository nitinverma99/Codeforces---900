verticl,horizontal = list(map(int, input().split()))
count = 0
while(min(verticl, horizontal)!=0):
    count += 1
    verticl -= 1
    horizontal -= 1
if count%2 ==0:
    print('Malvika')
else:
    print('Akshat')
