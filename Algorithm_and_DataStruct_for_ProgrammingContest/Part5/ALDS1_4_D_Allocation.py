T = []

def check(P):
    global k
    global n
    i = 0
    for j in range(k):
        s = 0
        while s + T[i] <= P:
            s += T[i]
            i += 1
            if i == n:
                return n
    return i

def solve():
    left = 0
    right = 100000 * 10000
    while (right - left) > 1:
        mid = (left + right) // 2
        v = check(mid) # mid == P を決めて何個積めるかチェック
        if v >= n :
            right = mid
        else:
            left = mid
    return right

input_line = list(map(int,input().split()))
n = input_line[0]
k = input_line[1]

for i in range(n):
    T.append(int(input()))

ans = solve()

print(ans)