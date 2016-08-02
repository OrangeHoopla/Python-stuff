word_len = 2
width = 3
height = 2
rectangle_width = word_len * width - (width - 1)
rectangle_height = word_len * height - (height - 1)
rectangle = [[" "] * rectangle_width for i in range(rectangle_height)]

for line in rectangle:
	print (rectangle)