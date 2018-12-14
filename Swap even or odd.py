b = input("Enter the String:")
f=''.join([d[1] + d[0] for d in zip(b[::2], b[1::2])])
print(f)
