for cases in range(int(input())):
    k = int(input())
    count = 0
    for i in range(2, 30):
        if k%((2**(i))-1) ==0:
            print(int(k/((2**(i))-1)))
            break
        else:
            continue