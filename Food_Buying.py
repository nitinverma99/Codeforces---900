for cases in range(int(input())):
    k = int(input())
    count = k
    if k<10:
        print(k)
    else:
        while(k != 0):
            value = k//10
            count += value
            k = value + k%10
            if k < 10:
                break
            else:
                continue
        print(count)
