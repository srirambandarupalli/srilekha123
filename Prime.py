t=int(input(""))
b=0
for x in range(1,t+1):
   if(t%x==0):
    b=b+1
if(b==2):
    print("yes")
else:
    print("no")
