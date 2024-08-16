T = int(input())

for _ in range(T):
    R, string = input().split()
    ans = ""
    for s in string:
        ans += s * int(R)
    print(ans)
