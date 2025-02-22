n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    a.append(list(map(int,list(input()))))
for i in range(n):
    b.append(list(map(int,list(input()))))


def flip(a, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if a[i][j] == 0:
                a[i][j] = 1
            else:
                a[i][j] = 0
    return a
def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True

result = 0
for i in range(0, n-2):
    for j in range(0, m-2):
        if a[i][j] != b[i][j]:
            a = flip(a, i, j)
            result += 1
if check() == False:
    print(-1)
else:
    print(result)
