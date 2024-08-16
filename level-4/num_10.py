import sys

N = int(sys.stdin.readline())
subjects = list(map(int,sys.stdin.readline().split()))

x = max(subjects)
total_score = 0
for i in range(len(subjects)):
    total_score += subjects[i] * 100 / x

print(total_score/len(subjects))