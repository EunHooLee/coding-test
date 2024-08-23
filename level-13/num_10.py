import sys

sys.stdin = open('input.txt','r')

profiles = []
for _ in range(int(sys.stdin.readline())):
    age, name = sys.stdin.readline().rstrip().split()
    profiles.append([int(age), name])

for p in sorted(profiles, key= lambda x:x[0]):
    print(p[0], p[1])
