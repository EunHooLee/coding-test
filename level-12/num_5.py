# 이 코드가 왜 틀린지 알고싶다.

# N = int(input())

# numbers = []
# num, length = 0, 1
# while True:
#     if len(str(num)) - length > 0:
#         if len(numbers) >= N:
#             break
#         length += 1

#     num_list = list(str(num))
#     for i in range(length+1):
#         temp_list = num_list.copy()
#         temp_list.insert(i,"666")
#         num_new = int(''.join(temp_list))
#         if  num_new not in numbers:
#             numbers.append(num_new)

#     num += 1
# print(sorted(numbers))
# print(sorted(numbers)[N-1])

N = int(input())
    
num, cnt = 1, 0
while True:
    if "666" in str(num):
        cnt += 1
    
    if cnt == N:
        print(num)
        break
    num+=1