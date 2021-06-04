for cases in range(int(input())):
    n = int(input())
    lst = []
    if n%2 == 0:
        print('1'*(n//2))

    else:
        print('7'+ (((n-3)//2)*'1'))
