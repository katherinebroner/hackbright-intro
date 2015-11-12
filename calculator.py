def add (num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply (num1, num2):
	return num1 * num2

def divide(num1,num2):
	return num1/num2

def modulo (num1, num2):
	return num1 % num2

def power(base,exponent):
	return base ** exponent

def square (num):
	return num ** 2

age = add(30,4)
height = subtract(78,2)
weight = multiply(6,24)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

