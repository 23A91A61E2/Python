a=list(map(int,input().split()))
count=0
for i in range(4):
  if a[i]>=10:
    count+=1
print(count)
