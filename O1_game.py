for cases in range(int(input())):
    s = input()
    count = 0
    while(s.count('01')> 0 or s.count('10') > 0):
        if s.count('01') > 0:
            s = s.replace('01', '', 1)
            count += 1
        elif s.count('10') > 0:
            s = s.replace('10', '', 1)
            count += 1
        else:
            break
    if count%2 == 0:
        print("NET")
    else:
        print("DA")