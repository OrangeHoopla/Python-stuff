def pythagoreancheck(a,b,c):
	if a + b + c ==1000:
		return True
	else: return False
def pythagorean():
	
	
	for i in range(0,1000):
		a = i
		for j in range(0,1000):
			b = j
			c = b**2 + a**2
			c = c**(.5)

			if pythagoreancheck(a,b,c):
				print a
				print b
				print c

if __name__ == '__main__':
	pythagorean()
