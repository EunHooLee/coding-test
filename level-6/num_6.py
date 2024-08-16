# solve 1
"""
string = input()
words = ["c=","c-","dz=","d-","lj","nj","s=","z="]

count = 0
pivot = 0

while len(string) > pivot:

    if string[pivot:pivot+3] in words:
        pivot+=3
    elif string[pivot:pivot+2] in words:
        pivot+=2
        
    else:
        pivot+=1
    count += 1

print(count)
"""

# solve 2
string = input()
words = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for w in words:
    string = string.replace(w,"*")
print(len(string))