def substitute(s: str, fro: str, to: str) -> None:
	cnt = 0
	l = len(s) - 1
	for i in range(len(s)):
		if s[i] == fro:
			cnt += 1
	s += " " * (cnt * (len(to) - len(fro)))
	r = len(s) - 1
	while l < r:
		if s[l] != fro:
			s[r] = s[l]
			r -= 1
			l -= 1
		else:
			for i in range(len(to) - 1, -1, -1):
				s[r] = to[i]
				r -= 1
			l -= 1

s = input()
fro = input()
to = input()
substitute(s, fro, to)
print(s)