t = input("")
u = [t[0]]
for v in t :
    if v not in u :
        u.append(v)
t2 = ''.join(u)
print(t2)
