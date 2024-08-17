# solition 1
"""
N = int(input())

ans = 0
for _ in range(N):
    word = list(input())
    word_list = list(set(word))
    word_count_list = [0]*len(word_list)
    
    for i in range(len(word_list)):
        pivot = word.index(word_list[i])
        word_count_list[i] = word.count(word_list[i])

        for j in range(pivot,pivot+word_count_list[i]):
            if word_list[i] == word[j]:
                word_count_list[i] -= 1
    
    if sum(word_count_list) == 0:
        ans += 1
print(ans)

"""

# 웃긴점은 아래 방법이 시간이 더 오래걸린다. (36ms -> 40ms)
ans = 0
for _ in range(int(input())):
    word = input()

    if list(word) == sorted(word, key=word.index):
        ans +=1
print(ans)