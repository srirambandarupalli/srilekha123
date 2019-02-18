r=int(input())
s=list(map(int,input().split()))
d=1
l=[]
for y in range(1,len(s)):
    if(s[x]>s[x-1]):
        d=d+1
    else:
        l.append(d)
        d=1
l.append(d)
print(max(l
