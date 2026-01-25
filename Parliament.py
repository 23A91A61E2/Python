t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    if 2*x>=n:
        print('YES')
    else:
        print('NO')
