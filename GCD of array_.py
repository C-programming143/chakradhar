def gcd(a,b):    
        if b%a==0:
            return a
        else:
            gcd(b%a,a)
a=[4,16,36,216]
a.sort()
res=a[0]
for i in a[1:]:
    res=gcd(res,i)
print(res)    
