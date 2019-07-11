def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v

def shellSort(A, n):
    h = 1
    while True:
        if h > n:
            break
        G.append(h)
        h = 3 * h  + 1
    for i in reversed(range(0, len(G)-1)):
        insertionSort(A, n, G[i])

n = int(input())
A = list(map(int,input().split()))

G = []
cnt = 0

shellSort(A, n)
print(len(G))

for i in reversed(range(0, len(G))):
    print(G[i], end="")
    if i != 0:
        print(" ", end="")
    else:
        print()

print(cnt)

for i in range(n):
    if i != 0:
        print(" ", end="")
    print(A[i], end="")
print()