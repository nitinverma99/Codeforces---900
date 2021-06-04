s = input()
gst = []
i = 0
s = s.replace('WUB', ' ')
s = s.strip(' ')
lst = list(s.split(' '))
count = lst.count('')
for i in range(count):
    lst.remove('')
print(' '.join(lst))
