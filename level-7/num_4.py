import sys

sys.stdin = open('input.txt','r')

M = [[0]*101] * 101

for _ in range(int(input())):
    x, y = map(int, input().split())
    
    for i in range(x,x+10):
        for j in range(y,y+10):
            M[i][j] = 1
            
        
ans=0
for row in M:
    ans += sum(row)
print(ans)

