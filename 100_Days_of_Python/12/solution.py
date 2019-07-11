res, l, r = 0, 0, len(height)-1
while(l<r):
	mn = min(height[l], height[r])
	if(height[l]==mn):
		l+=1
		while(l<r and height[l]<mn):
			res+=mn-height[l]
			l+=1
	else:
		r-=1
		while(l<r and height[r]<mn):
			res+=mn-height[r]
			r-=1
return res
