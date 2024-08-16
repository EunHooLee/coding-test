S = input()

pivot = ord('a')
arr = [-1]*26

for i in range(len(S)):
    idx = ord(S[i]) - pivot
    if arr[idx] == -1:
        arr[idx] = i
print(*arr)