for i in range(1,11):
	for j in range(1,11):
		print(i*j, end = " ")
	print()
import time

N = int(input())
k = int(input())

stW = 1
enW = N
stH = 1
enH = N

while stW<=enW and stH<=enH:
	width = (stW + enW) // 2
	height = (stH + enH) // 2
	cctv = width*height

	if k > cctv:
		stW = width + 1
		stH = height + 1

	elif k < cctv:
		enW = width - 1
		enH = height - 1

	else:
		enW = width + 1
		stH = height - 1
	time.sleep(0.2)
	print(cctv,width,height)