t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    total_songs=n//x 
    print(total_songs//3)
