n = int(input())
if n>=0:
    print(n)
else:
    n = str(n)
    n = n[::-1]
    l = len(n)
    if int(n[0]) > int(n[1]):
        n = n.replace(n[0], '', 1)
    else:
        n = n.replace(n[1], '',1)
    n = n[::-1]
    print(int(n))