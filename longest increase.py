m=int(input())
y=list(map(int,input().split()))
b=1
s=[]
for x in range(1,len(y)):
    if(y[x]>=y[x-1]):
        b=b+1
    else:
        s.append(b)
        b=1
s.append(b)
print(max(s))
