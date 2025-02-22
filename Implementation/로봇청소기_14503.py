"""
1. 아이디어
- 현재 칸이 0이면 1로 바꿈
- for문으로 주변 4칸을 탐색
- 청소되지 않은 칸 없으면 한 칸 후진, 뒤가 벽이면 중지
- 청소되지 않은 칸 있으면 반시계 방향으로 90도 회전, 앞 칸이 청소되지 않았으면 한 칸 전진
2. 시간복잡도
- O(NM)
- 50 * 50 = 2500 < 2억
3. 자료구조
- map int[][]
- dx, dy int[]
- 칸의 개수 카운트, x, y, d
"""

n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

while 1:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if a[x][y] == 0:
        a[x][y] = 2
        result += 1
    sw = False
    for i in range(1,5):
        nx = x + dx[d-i]
        ny = y + dy[d-i]
        if 0<= nx < n and 0 <= ny < m:
            # 청소되지 않은 칸이 있으면 sw = True
            if a[nx][ny] == 0:
                sw = True
                # 반시계 방향으로 90도 회전
                d = (d - i + 4) % 4
                x = nx
                y = ny
                break
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if sw == False:
        nx = x - dx[d]
        ny = y - dy[d]
        if 0<= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1:
                break
            else:
                x = nx
                y = ny
        else:
            break
print(result)

