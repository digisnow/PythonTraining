"""
input n (ex: 10)
input A (ex: 8 5 9 2 6 3 7 1 10 4)
"""

def merge(A, n, left, mid, right):
    global L
    global R
    global cnt
    n1 = mid - left
    n2 = right - mid
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
    L[n1] = 200000000
    R[n2] = 200000000
    i = 0
    j = 0
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1

def mergeSort(A, n, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, n, left, mid)
        mergeSort(A, n, mid, right)
        merge(A, n, left, mid, right)

cnt = 0
n = int(input())
A = list(map(int,input().split()))
L = [200000] * 50
R = [200000] * 50
mergeSort(A, n, 0, n)

for s in A:
  print(s, end =" ")
print()
print(cnt)