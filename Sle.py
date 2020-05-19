n=int(input())
data=list(map(int,input().split()))

data=list(set(data))

data.sort()

print(data[-2])
