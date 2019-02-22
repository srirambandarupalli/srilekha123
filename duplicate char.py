a = input("")
b = [a[0]]
for c in a :
    if c not in b :
        b.append(c)
a2 = ''.join(b)
print(a2)
