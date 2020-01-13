T=int(input())
N,K=(map(int,input().split()))
c=0
for i in range(T):
     if K>=N:
          c+=1
          for j in range(N):
               q=(map(int,input().split()))
     print(c)

else:
     print("0")
