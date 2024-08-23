N = int(input())

generator = 0
for i in range(N):
    sub_sum = 0
    current = str(i)
    for j in current:
        sub_sum += int(j)
    if N - i - sub_sum == 0:
        generator = i
        break
    
print(generator)