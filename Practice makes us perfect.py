p = list(map(int, input().split()))
print(sum(x >= 10 for x in p))
