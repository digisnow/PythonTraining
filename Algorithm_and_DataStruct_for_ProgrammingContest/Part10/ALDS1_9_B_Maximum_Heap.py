"""
input H (ex: 10)
input A (ex: 4 1 3 2 16 9 10 14 8 7)
"""

MAX = 2000000

def maxHeapify(i):
    global A
    global H
    l = 2 * i
    r = 2 * i + 1

    # 左の子、自分、右の子で値が最大ノードを選ぶ
    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r <= H and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(largest)

H = int(input())
A = list(map(int,input().split()))
A.insert(0, 0)

for i in reversed(range(1, H//2)):
    maxHeapify(i)

for i in range(1, H+1):
    if i != 1:
        print(" ",end="")
    print(str(A[i]),end="")
print()