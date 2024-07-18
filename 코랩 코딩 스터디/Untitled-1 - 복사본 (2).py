# (세현)

def solution(m,musicinfos):
	answer = '(None)'
	m = m.replace('A#','X').replace('C#','Y').replace('D#','J').replace('F#','K').replace('G#','L').replace("B#","Z")
	longest = 0
	for info in musicinfos:
		st,en,name,muse = info.split(',')
		st,en = st.split(':'),en.split(':')
		time = (int(en[0])-int(st[0])) * 60 + int(en[1])-int(st[1])
		muse = muse.replace('A#','X').replace('C#','Y').replace('D#','J').replace('F#','K').replace('G#','L').replace("B#","Z")
		muse = muse * (time // len(muse)) + muse[0:time % len(muse)]

		if m in muse:
			if time > longest:
				longest = time
				answer = name
	return answer