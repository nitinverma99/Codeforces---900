n,d = list(map(int, input().split()))
lst = list(map(int, input().split()))
songsWithJokes = sum(lst) + (n-1)*10
if songsWithJokes > d:
    print('-1')
else:
    print(2*n -2 + ((d-songsWithJokes)//5))

    