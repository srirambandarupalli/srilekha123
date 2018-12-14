b = input("Enter the String:")
f=''.join([c[1] + c[0] for c in zip(b[::2], b[1::2])])
print(f)
