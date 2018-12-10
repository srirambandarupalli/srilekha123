n=int(input(""))
s=list(map(int,str(n)))
k=list(map(lambda x:x**3,s))
if(sum(k)==n):
    print("yes")
else:
    print("no")

