"""
input n (ex: 6)
input A (ex: D3 H2 D1 S3 D2 C1)
"""

import copy

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

def merge(A, n, left, mid, right):
    global L
    global R
    n1 = mid - left
    n2 = right - mid
    for i in range(n1):
        L[i] = copy.deepcopy(A[left + i])
    for i in range(n2):
        R[i] = copy.deepcopy(A[mid + i])
    L[n1].value = 200000000
    R[n2].value = 200000000
    i = 0
    j = 0
    for k in range(left, right):
        if L[i].value <= R[j].value:
            A[k] = copy.deepcopy(L[i])
            i += 1
        else:
            A[k] = copy.deepcopy(R[j])
            j += 1

def mergeSort(A, n, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, n, left, mid)
        mergeSort(A, n, mid, right)
        merge(A, n, left, mid, right)

def partition(A, n, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j].value <= x.value:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quickSort(A, n, p, r):
    if p < r:
        q = partition(A, n, p, r)
        quickSort(A, n, p, q-1)
        quickSort(A, n, q+1, r)

def printCard(A, N):
    for i in range(N):
        if i > 0:
            print(" ", end="")
        print(A[i].suit + str(A[i].value), end="")
    print()

n = int(input())
Z = input().split()
A = [Card("", 0)]*n
B = [Card("", 0)]*n
stable = 1

L = [Card("", 300000)] * 1000
R = [Card("", 300000)] * 1000

for i in range(n):
    A[i] = Card(Z[i][0], int(Z[i][1]))

B = copy.deepcopy(A)

mergeSort(A, n, 0, n)
quickSort(B, n, 0, n-1)

for i in range(n):
    if A[i].suit != B[i].suit:
        stable = 0

if stable == 1:
    print("Stable")
else:
    print("Not Stable")

printCard(A, n)
printCard(B, n)
