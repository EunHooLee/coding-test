# solve 1
"""
word = input()

num = [0] * 26

for i in range(len(num)):
    for w in word:
        if ord(w) ==i+65 or ord(w)==i+97:
            num[i]+=1

cnt = 0
for i in num:
    if i == max(num):
        cnt +=1 
if cnt > 1:
    print("?")
else:
    print(chr(65+num.index(max(num))))

"""

word = input().upper()
word_list = list(set(word))

count_list = []
for w in word_list:
    count_list.append(word.count(w))

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    print(word_list[count_list.index(max(count_list))])