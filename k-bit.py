import sys, string, math
M= int(input())
O = 2**M
S = []
for i in range(0,O) :
    T = bin(i)[2:]
    j = len(T)
    if j < M :
        T = '0' * (M-j) + T
    S.append(T)
for i in range(0,len(S)) :
    print(S[i])
