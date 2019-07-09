def selectionSort(A, N):
    sw = 0
    for i in range(N-1):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        A[i], A[minj] = A[minj], A[i]
        if i != minj:
            sw += 1
    return sw

N = int(input())
A = list(map(int,input().split()))
sw = selectionSort(A, N)

for i in range(N):
    if i > 0:
        print(" ", end="")
    print(A[i], end="")
print()
print(sw)