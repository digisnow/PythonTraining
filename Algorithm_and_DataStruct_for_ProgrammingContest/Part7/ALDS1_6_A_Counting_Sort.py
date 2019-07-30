"""
input n (ex: 7)
input A (ex: 2 5 1 3 2 3 0)
"""

MAX = 2000001
n = int(input())
A = list(map(int,input().split()))
A.insert(0, 0)
C = [0]*MAX
B = [0]*(n+1)
for i in range(n):
    C[A[i+1]] += 1

for i in range(1, MAX):
    C[i] = C[i] + C[i-1]

for j in range(1, n+1):
    B[C[A[j]]] = A[j]
    C[A[j]] -= 1

for i in range(1, n+1):
    if i > 1:
        print(" ", end="")
    print(B[i], end="")
print()