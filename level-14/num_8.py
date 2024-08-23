import sys

S = sys.stdin.readline().rstrip()

sub_S = set()

for i in range(len(S)):
    for j in range(i+1,len(S)+1):
        sub_S.add(S[i:j])
print(len(sub_S))
