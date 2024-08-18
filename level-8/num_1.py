N, B = input().split()

number = ['0','1','2','3','4','5','6','7','8','9']
ans = 0
for i, w in enumerate(N):
    if w in number:
        ans += int(w) * (int(B) ** (len(N)-1-i))
    else:
        ans += (ord(w) - 55) * (int(B) ** (len(N)-1-i))

print(ans)
