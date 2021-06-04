for cases in range(int(input())):
    a,b,c,d = list(map(int, input().split()))
    sum = 0
    time =0
    if a==b or b> a:
        print(b)
    else:
        a -= b
        time += b
        if c<=d :
            print('-1')
        else:
            remain = a%(c-d)
            if remain == 0:
                time += (a//(c-d))*c
            else:
                time += ((a//(c-d)) + 1)*c 
            print(time)
