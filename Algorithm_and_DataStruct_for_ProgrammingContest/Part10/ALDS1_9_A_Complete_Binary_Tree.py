"""
input H (ex: 5)
input A (ex: 7 8 1 2 3)
"""

MAX = 100000

def parent(i):
    return i // 2

def left(i):
    return  2 * i

def right(i):
    return 2 * i + 1

H = int(input())
A = list(map(int,input().split()))

A.insert(0, 0)

for i in range(1, H+1):
    print("node " + str(i) + ": key = " + str(A[i]) + ", ", end="")
    if parent(i) >= 1:
        print("parent key = " + str(A[parent(i)]) + ", ",end="")
    if left(i) <= H:
        print("left key = " + str(A[left(i)]) + ", ",end="")
    if right(i) <= H:
        print("right key = " + str(A[right(i)]) + ", ",end="")
    print()
