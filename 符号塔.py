for i in range(1,6):
	if i % 2 == 1:
		print(" "*(5-i), "*"*(2*i-1))
	else:
		print(" "*(5-i), "#"*(2*i-1))
