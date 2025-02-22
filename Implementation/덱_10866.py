import sys
input = sys.stdin.readline

n = int(input().rstrip())
q = []
for _ in range(n):
    s = list(input().split())
    if s[0] == 'push_front':
        q.insert(0, int(s[1]))
    elif s[0] == 'push_back':
        q.append(int(s[1]))
    elif s[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif s[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if len(q) == 0:
            print(-1)
        else: print(q[0])

    elif s[0] == 'back':
        if len(q) == 0: print(-1)
        else: print(q[-1])
