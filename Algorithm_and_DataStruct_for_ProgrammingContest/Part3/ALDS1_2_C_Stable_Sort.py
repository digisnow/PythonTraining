"""
input n (ex: 5)
input A (ex: H4 C9 S4 D2 C3)
"""

import copy
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

def bubble(A, N):
    for i in range(N-1):
        for j in reversed(range(i+1, N)):
            if A[j].value < A[j-1].value:
                A[j], A[j-1] = A[j-1], A[j]

def selection(A, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j].value < A[minj].value:
                minj = j
        A[i], A[minj] = A[minj], A[i]

def printCard(A, N):
    for i in range(N):
        if i > 0:
            print(" ", end="")
        print(A[i].suit + A[i].value, end="")
    print()

def isStable(C1, C2, N):
    for i in range(N):
        if C1[i].suit != C2[i].suit:
            return False
    return True

N = int(input())
A = input().split()
C1 = [Card("","")]*N
C2 = [Card("","")]*N

for i in range(N):
    C1[i] = Card(A[i][0], A[i][1])

C2 = copy.deepcopy(C1)

bubble(C1, N)
selection(C2, N)

printCard(C1, N)
print("Stable")

printCard(C2, N)

if isStable(C1, C2, N):
    print("Stable")
else:
    print("Not Stable")