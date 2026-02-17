t=int(input())
for _ in range(t):
    
    w,x,y,z=map(int,input().split())
    if w+(y*z)<x:
        print('Unfilled')
    elif w+(y*z)>x:
        print('overflow')
    else:
        print('filled')
    
