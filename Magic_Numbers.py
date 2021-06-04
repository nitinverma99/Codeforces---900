s = input()
i = 0
while(len(s) > 3):
    if s[0] =='1':
        if s[1] == '4':
            if s[2] == '4':
                    s = s.replace(s[0:3], '', 1)
            else:
                s = s.replace(s[0:2], '', 1)
        else:
            s = s.replace(s[0], '', 1)
    else:
        break
if s=="111" or s =="114" or s=="144" or s=="14" or s=="11" or s=="1" or s=="141":
    print("YES")
else:
    print("NO")