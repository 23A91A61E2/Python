t=int(input())
for _ in range(t):
    w,x,y,z=map(int,input().split())
    print(w+z*(x-y))
