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
	elif num2 > num3:
		print num2
	else:
		print num3

larger (8, 10, 12)

def smaller_1 (num1, num2):
	if num1<num2:
		print num1

smaller_1(False, True)

def smaller (num1, num2, num3):
	if num1 < num2:
		if num1 < num3:
			print num1
	elif num2 < num3:
		print num2
	else:
		print num3

smaller(10,8,21)