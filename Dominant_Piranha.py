for cases in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    maxx = max(lst)
    count = lst.count(maxx)
    if count == len(lst):
        print('-1')
    else:
        for i in range(len(lst)):
            if lst[i] == maxx:
                if i ==0:
                    if lst[0] > lst[1] :
                        print('1')
                        break
                elif i == len(lst)-1 :
                    if lst[len(lst)-1] > lst[len(lst)-2]:
                        print(len(lst))
                        break
                elif lst[i+1] < lst[i] or lst[i-1] < lst[i]:
                    print(i+1)
                    break
                else:
                    continue