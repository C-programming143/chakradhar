nc=int(input())
box=list(map(int,input().split()))
l=[]
for i in box:
    if i not in l:
        l.append(i)
        k=box.count(i)
        if(k%2!=0):
            print(i)
            break
