"""
1. 8x8 크기 자르기
2. 체크 무늬로 칠하는 개수 계산
3. 위 1,2 번 반복
4. 최솟값 출력

(i,j) 를 시작으로 행렬 짜르기

"""
import sys

sys.stdin = open('input.txt','r')

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input())

ans = 64
for i in range(N-7):
    for j in range(M-7):
        
        cnt = [0, 0]
        checker = ["WBWBWBWB", "BWBWBWBW"]
        # 시작점 선정완료
        
        # 한개의 보드 확인
        for k in range(8):
            row_of_sub_board = board[i+k][j:j+8]
            for v in range(8):
                if checker[k%2][v] != row_of_sub_board[v]:
                    cnt[0] += 1
                if checker[k%2==0][v] != row_of_sub_board[v]:
                    cnt[1] += 1
        if min(cnt) < ans:
            ans = min(cnt)
print(ans)