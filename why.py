def palin( x ):
	new = str(x)
	news = new[::-1]
	if news == new:
		return True
	else: return False
c = 0
for a in range(999,99,-1):
	print a
	for b in range(999,a,-1):
		
		d = a * b
		if(palin(d)) and d>c:
			c = d

print c
	