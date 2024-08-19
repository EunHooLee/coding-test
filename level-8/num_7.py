A, B, V = map(int, input().split())

# days, now = 0, 0
# while True:
#     days += 1
#     now += A
    
#     if now >= V:
#         print(days)
#         break
#     now -=B

"""
l = V - A 까지는 올라가야됨 (하루 추가)
B-A

"""


distance = V - A 
if distance % (A-B) == 0:
    print(distance // (A-B) + 1)
else:
    print(distance // (A-B) + 2)