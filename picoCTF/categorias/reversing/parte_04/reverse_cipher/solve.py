rev = open('rev_this').read()
flag = ''

for i in range(8):
	flag += rev[i]
for j in range(8, 24):
	if j & 1 == 0:
		flag += chr(ord(rev[j]) - 5)
	else:
		flag += chr(ord(rev[j]) + 2)
flag += rev[23]
print(flag)
