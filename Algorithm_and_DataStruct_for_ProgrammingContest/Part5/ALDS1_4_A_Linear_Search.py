def search(A, n, key):
    i = 0
    A.append(key)
    while A[i] != key:
        i += 1
    return i != n

sum = 0
A = []

n = int(input())
A = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

for i, key in enumerate(T):
    if search(A, n, key):
        sum += 1
print(sum)