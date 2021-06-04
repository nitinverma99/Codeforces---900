for cases in range(int(input())):
    n = int(input())
    count = 0
    for i in range(3,10,2):
        if n%i == 0:
            print("YES")
            count=1
            break
    if count == 0 :
        print("NO")