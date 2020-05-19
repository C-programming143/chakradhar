string=input()
string=list(string)
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if string[i]>string[j]:
            string[i],string[j]=string[j],string[i]
sorted_string=""
sorted_string="".join(string)
print(sorted_string)
