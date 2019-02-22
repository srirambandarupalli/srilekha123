b=int(input())
r=0
while(b>0):
    b1=int(b%10)
    s=(b1*b1)+r
    b=int(b/10)
print(r)
