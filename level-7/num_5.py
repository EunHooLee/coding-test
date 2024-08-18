import sys
"""
- 좌표값은 그 값을 넓이가 1인 사각형의 좌측 하단 좌표
- 즉 좌표의 최솟값은 1 이고, 사각형의 크기는 100이기 때문에 1+100-1 인 100까지만 존재하면 된다.
- 다시말하면, 좌표의 최솟값 1, 최댓값 100 이라서 행렬로 만든다면 0~101까지 해야된다. (100,100)이 존재해야되기 때문에
"""

sys.stdin = open('input.txt','r')

paper = [[0]* 101 for _ in range(101)]
ans = 0

for _ in range(int(input())):
    x, y = map(int, input().split())

    # y 는 행 / x 는 열
    for i in range(y, y+10):
        paper[i][x:x+10] = [1] * 10
            

for row in paper:
    ans += sum(row)
print(ans)

