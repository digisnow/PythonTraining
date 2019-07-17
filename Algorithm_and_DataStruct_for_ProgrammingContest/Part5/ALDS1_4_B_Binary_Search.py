def binarySearch(key):
    global A
    global n
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if key == A[mid]:
            # find Key
            return 1
        if key > A[mid]:
            # search second half
            left = mid + 1
        elif key < A[mid]:
            # search first half
            right = mid
    return 0

sum = 0
n = int(input())
A = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

for i, key in enumerate(T):
    if binarySearch(key):
        sum += 1
print(sum)