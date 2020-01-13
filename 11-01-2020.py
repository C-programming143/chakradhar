n,m=map(int,input().split())
l,a,b=[],[],[]
for i in range(n):
    l.append(int(input()))
for j in range(n):
    if l[j]>m:
        a=l[:j]
        break
for k in range(n-1,-1,-1):
    if l[k]>m:
        b=l[n-1:k:-1]
        break
print(abs((len(a)+len(b))-len(l)))
