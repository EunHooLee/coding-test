N, B = map(int, input().split())

number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""

while N:
    ans += number[N%B]
    N //=B

print(ans[::-1])