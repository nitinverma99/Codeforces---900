inp = input()
s = 'qwertyuiopasdfghjkl;zxcvbnm,./'
lst = list(s)
string = input()
gst = []
for i in range(len(string)):
    index = lst.index(string[i])
    if inp == 'R':
        gst.append(lst[index-1])
    else:
        gst.append(lst[index+1])
print(''.join(gst))