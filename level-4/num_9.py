N, M = map(int, input().split())
basket = list(range(N+1))
for _ in range(M):
    i, j = map(int, input().split())
    basket[i:j+1] = basket[j:i-1:-1]

for i in range(1, N+1):
    print(basket[i], end=" ")
