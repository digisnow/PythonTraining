"""
input n (ex: 12)
input A (ex: 13 19 9 5 12 8 7 4 21 2 6 11)
output List (ex. 9 5 8 7 4 2 6 [11] 21 13 19 12)
"""

def partition(p, r):
    global A
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

n = int(input())
A = list(map(int,input().split()))
q = partition(0, n-1)

for i in range(n):
    if i != 0:
        print(" ", end="")
    if i == q:
        print("[", end="")
    print(A[i], end="")
    if i == q:
        print("]", end="")
print()