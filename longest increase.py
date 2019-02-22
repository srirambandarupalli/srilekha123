num=int(input())
n=list(map(int,input().split()))
r=0
l=[]
for i in range(0,len(n)-1):
	if int(n[i+1])>=int(n[i]):
		r=r+1
	else:
		l.append(r)
		r=0
print(max(l)+1)
