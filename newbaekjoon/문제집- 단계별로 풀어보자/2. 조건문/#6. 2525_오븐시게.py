a, b = map(int, input().split(" "))
c = int(input())
now = a*60+ b
done = now + c
if done  >= 24*60:
    print((done//60)-24, done % 60)
else:
     print((done//60), done % 60)