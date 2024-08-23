N = int(input())

ans, x = 10000, 0
while N-5*x >= 0:
    if (N-5*x)%3 == 0:
        y = (N-5*x)/3
        if x+y <= ans:
            ans = int(x+y)
    x+=1

if ans == 10000:
    print(-1)
else:
    print(ans)