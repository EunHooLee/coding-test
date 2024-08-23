"""
i j k
1 

"""
# Fail 1

# n = int(input())
# sum = 0
# for i in range(1,n-1):
#     sub_sum = 0
#     for j in range(i+1,n):
#         sub_sum += (n - (1+j) + 1)
    
    
#     sum += sub_sum
    
# print(sum)
# print(3)

# Fail 2

# n = int(input())
# sum = 0
# for i in range(1,n-1):
#     # sum += n*(n-1)/2 - (n*i - i*(i+1)/2)
#     sum += (n-i-1)*(n-i) / 2
# print(int(sum))
# print(3)

# 다시풀기


# nC3
n = int(input())
print(int(n*(n-1)*(n-2)/6))
print(3)