def solve(i, m):
    global n
    global A
    if m == 0:
        return 1
    if i >= n:
        return 0
    res = solve(i+1, m) or solve(i+1, m-A[i])
    return res

n = int(input())
A = list(map(int,input().split()))
q = int(input())
M = list(map(int,input().split()))

for i in range(len(M)):
    ret = solve(0, M[i])
    if ret == 1:
        print("yes")
    else:
        print("no")
