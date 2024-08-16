arr = []
B = 42
for _ in range(10):
    A = int(input())
    arr.append(A%B)
ans = set(arr)
print(len(ans))