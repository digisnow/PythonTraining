import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def koch(n, a, b):
    if n == 0:
        return
    th = math.pi * 60.0 / 180.0 # 度からラジアンへ単位を変換

    s = Point((2.0 * a.x + 1.0 * b.x) / 3.0, (2.0 * a.y + 1.0 * b.y) / 3.0)
    t = Point((1.0 * a.x + 2.0 * b.x) / 3.0, (1.0 * a.y + 2.0 * b.y) / 3.0)
    u = Point((t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x, (t.x - s.x) * math.sin(th) + (t.y - s.y) * math.cos(th) + s.y)

    koch(n-1, a, s)
    print(str(round(s.x, 8)) + " " + str(round(s.y, 8)))
    koch(n-1, s, u)
    print(str(round(u.x, 8)) + " " + str(round(u.y, 8)))
    koch(n-1, u, t)
    print(str(round(t.x, 8)) + " " + str(round(t.y, 8)))
    koch(n-1, t, b)

a = Point(0, 0)
b = Point(100, 0)

n = int(input())

print(str(a.x) + " " + str(a.y))
koch(n, a, b)
print(str(b.x) + " " + str(b.y))