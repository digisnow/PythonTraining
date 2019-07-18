import copy

M = 1046527
NIL = -1
L = 14
H = [[] for j in range(M)]

def getChar(ch):
    if ch == 'A':
        return 1
    elif ch == 'C':
        return 2
    elif ch == 'G':
        return 3
    elif ch == 'T':
        return 4
    else:
        return 0

def getKey(str0):
    sum = 0
    p = 1
    for i in range(len(str0)):
        sum += p * (getChar(str0[i]))
        p *= 5
    return sum

def h1(key):
    global M
    return key % M

def h2(key):
    return (1 + (key % (M - 1)))

def find(str0):
    global H
    key = getKey(str0)
    i = 0
    while True:
        h = (h1(key) + i * h2(key)) % M
        if len(H[h]) == 0:
            return 0
        elif H[h] == str0:
            return 1
        i += 1
    return 0

def insert(str0):
    global H
    key = getKey(str0)
    i = 0
    while True:
        h = (h1(key) + i * h2(key)) % M
        if len(H[h]) == 0:
            H[h] = copy.copy(str0)
            return 0
        elif H[h] == str0:
            return 1
        i += 1
    return 0

char = []
com = []


n = int(input())
for i in range(n):
    com, str0 = input().split()

    if com[0] == 'i':
        insert(str0)
    else:
        if find(str0):
            print("yes")
        else:
            print("no")

