for cases in range(int(input())):
    k = int(input())
    if k==1:
        print('0')
    else:
        count = 0
        while(k>0):
            if k%6 == 0:
                k = k//6
                count += 1
            elif k%3 ==0:
                k = 2*k
                k = (k)//6
                count +=2
            elif k ==1:
                print(count)
                break
            else:
                print('-1')
                break
        
    