for cases in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    gst = []
    for i in range(max(lst)+2):
        if lst.count(i) == 0:
            gst.append(i)    
            gst.append(i)
            break
        elif lst.count(i) == 1:
            gst.append(i)
        else:
            continue
        if len(gst) >=2 :
            break
    print(gst[0] + gst[1])
    
    
