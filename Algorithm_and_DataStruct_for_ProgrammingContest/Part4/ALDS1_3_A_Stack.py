top = 0
S = []
def push(x):
    S.append(x)

def pop():
    return(S.pop())

s = input().split()

for c in s:
    if c == '+':
        a = pop()
        b = pop()
        push(a + b)
    elif c == '-':
        b = pop()
        a = pop()
        push(a - b)
    elif c == '*':
        a = pop()
        b = pop()
        push(a * b)
    else:
        push(int(c))

print(pop())