N = int(input())
height = 1
max = 1
while True:
    if N <= max:
        print(height)
        break
    max += 6*height
    height +=1