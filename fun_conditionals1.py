def check_for_string (input):
	if type(input) == str:
		print input, "is a string"
	else: 
		print input, "is not a string."
check_for_string (8)

def larger (num1, num2, num3):
	if num1 > num2:
		if num1 > num3:
			print num1
		else:
			print num3
	else:
		print num2

larger (4,63,32)

def smaller (num1, num2, num3):
	if num1 < num2:
		if num1 < num3:
			print num1
		else:
			print num3
	else: 
		print num2

smaller (4,63,32)
	