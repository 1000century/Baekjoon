x = []
y = []
for _ in range(3):
    a, b = map(int,input().split())
    x.append(a)
    y.append(b)
x_two = list(set(x))
y_two = list(set(y))
sum_x = 0
sum_y = 0
sum_x_two = 0
sum_y_two = 0
for _ in x:
    sum_x = sum_x + _
for _ in y:
    sum_y = sum_y + _
for _ in x_two:
    sum_x_two = sum_x_two + _
for _ in y_two:
    sum_y_two = sum_y_two + _
result_x = sum_x_two * 2 - sum_x
result_y = sum_y_two * 2 - sum_y
print(result_x,result_y,sep= " ")
