
submitted = []
for _ in range(28):
    submitted.append(int(input()))
submitted.append(int(0))
submitted.append(int(0))
submitted = sorted(submitted)

total = []
for _ in range(1,31):
    total.append(int(_))

for i in range(30):
    submit = submitted
    if submit[i] == total[i]:
        continue
    else:
        print(total[i])
        submit.insert(i,total[i])