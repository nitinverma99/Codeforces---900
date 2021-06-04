s = input()
if len(s) >= 7:
    for i in range(len(s)-6):
        if s[i:7+i] == '1111111' or s[i:7+i] == '0000000':
            print("YES")
            break
        elif i == len(s)-7 :
            print("NO")
            break
        else:
            continue
else:
    print("NO")