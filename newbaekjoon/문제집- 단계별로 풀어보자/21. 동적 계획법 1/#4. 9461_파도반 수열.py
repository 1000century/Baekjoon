T = int(input())
tests = []

wave = [0,1,1,1,2,2]
for i in range(6,101):
	wave.append(wave[i-1] + wave[i-5])
for _ in range(T):
	print(wave[int(input())])