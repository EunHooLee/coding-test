string = input()
arr = ['ABC', 'DEF', 'GHI','JKL','MNO','PQRS','TUV','WXYZ']

time = 0
for s in string:
    for i in range(len(arr)):
        if s in arr[i]:
            time += i + 3

print(time)