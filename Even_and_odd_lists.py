l=list(map(int,input().split()))
p=[]
q=[]
for i in l:
      if(i%2==0):
            p.append(i)
      else:
            q.append(i)
print('even',p)
print('odd',q)
