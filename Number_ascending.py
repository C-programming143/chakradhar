num=int(input())
num=str(num)
st=[int(i) for i in num]#string into int list
st.sort()#sort
num=[str(i) for i in st]#int list into str list
st=""
st=int("".join(num))#str list into string, then converting into integer
print(st)
