l1,m=map(int,input().split())
l=input().split()
while(m>0):
    l.insert(0,l.pop())
    m=m-1
for i in range(0,len(l)):
    if(i!=len(l)-1):
        print(l[i],end=(" "))
    else:
        print(l[i])
