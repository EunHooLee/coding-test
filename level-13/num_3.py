N, k = map(int, input().split())
scores = list(map(int, input().split()))

print(sorted(scores, key=lambda x:-x)[k-1])