N, M = map(int, input().split())

A, B = [0] * N, [0] * N

for i in range(N):
    A[i] = list(map(int, input().split()))

for i in range(N):
    B[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=" ")
    print("")
    
