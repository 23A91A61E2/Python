for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        print('loss')
    elif a==b:
        print('neutral')
    else:
        print('profit')
