def bubbleSort(A, N):
    sw = 0
    flag = True
    i = 0
    while flag:
        flag = False
        for j in reversed(range(i+1, N)):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1
                sw += 1
        i += 1
    return sw

N = int(input())
A = list(map(int,input().split()))
sw = bubbleSort(A, N)

for i in range(N):
    if i != 0:
        print(" ", end="")
    print(A[i], end="")
print()
print(sw)