"""
1. 아이디어
- for를 돌면서 현재 중요도와 max중요도 같은 문서 있는지 확인
- 같다면 문서를 출력
- 같지 않다면 현재 문서를 맨 뒤에 삽입
2. 시간복잡도
- O(N!)
- 100! < 2억 가능
3. 자료구조
- queue int[]
- 테스트 개수, 문서 개수, 찾을 문서 위치
"""

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    result = 1
    while a:
        if a[0] < max(a):
            a.append(a.pop(0))
        else:
            if m == 0: break
            # 출력
            a.pop(0)
            result += 1
        m = m-1 if m>0 else len(a)-1
    print(result)