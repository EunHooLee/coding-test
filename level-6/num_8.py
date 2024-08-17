template = {"A+":4.5, "A0":4.0,"B+":3.5, "B0":3.0,"C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0,"F":0.0}

num, den = 0, 0
for _ in range(20):
    subject, score, rank = input().split()
    if rank == "P":
        continue

    num += float(score) * template[rank]
    den += float(score)
print(num/den)
