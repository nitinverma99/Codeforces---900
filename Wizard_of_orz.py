lst = [0,1,2,3,4,5,6,7,8,9] * 25000
for cases in range(int(input())):
    n = int(input())
    value = '989'
    if n<4:
        print(value[:n])
    else:
        string = lst[:n-3]
        for i in range(len(string)):
            string[i] = str(string[i])
        value = value + ''.join(string)
        print(value)
