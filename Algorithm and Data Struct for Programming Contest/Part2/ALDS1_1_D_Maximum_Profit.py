MAX = 200000
n = int(input())
num_list = [input() for i in range(n)]
num_list = list(map(int, num_list))

maxv = -2000000000
minv = num_list[0]

for i in range(1, n):
    maxv = max(maxv, num_list[i] - minv)
    minv = min(minv, num_list[i])

print(maxv)