t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    pairs=min(x,z)+(y//2)
    print(pairs)
