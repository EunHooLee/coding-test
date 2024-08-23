import sys

sys.stdin = open('input.txt','r')

words = []
for _ in range(int(sys.stdin.readline())):
    w = sys.stdin.readline().rstrip()
    if w not in words:
        words.append(w)

for w in sorted(words,key=lambda x: (len(x),x)):
    print(w)
