sum_angle = 0
angles = []

for _ in range(3):
    angle = int(input())
    sum_angle += angle
    angles.append(angle)

if sum_angle != 180:
    print('Error')
else:
    if len(set(angles)) == 1:
        print('Equilateral')
    elif len(set(angles)) == 2:
        print('Isosceles')
    else:
        print("Scalene")
