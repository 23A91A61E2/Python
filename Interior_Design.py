for _ in range(int(input())):
    X1,Y1,X2,Y2=map(int,input().split())
    c=(X1+Y1)
    d=(X2+Y2)
    if c<=d:
        print(c)
    else:
        print(d)
