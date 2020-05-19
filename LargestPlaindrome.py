def palindrome(n):
    n1=n
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    if rev==n1:
        return 1
    else:
        return 0
    
def largestpalindrome(data):
    maxx=0
    for i in data:
        res=palindrome(i)
        if res==1:
            if maxx<i:
                maxx=i
    return maxx
    

n=int(input())#size of the list
data=list(map(int,input().split()))# list values
large=largestpalindrome(data)
print(large)
