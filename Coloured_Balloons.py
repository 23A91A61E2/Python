T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    total_cost=0
    for i in range(N):
        total_cost+=A[i]*(i+1)
    print(total_cost)
    
