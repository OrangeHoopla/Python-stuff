def sumsquares(n):
	tot = 0
	for i in range(0,n+1):
		tot += i**2
	return tot
def squaresums(n):
	tot1 = 0
	for i in range(0,n+1):
		tot1 += i
	return tot1**2
print squaresums(100)-sumsquares(100)