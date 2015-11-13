def find_average (num1, num2, num3):
    if type(num1) == int and type(num2) == int and type(num3) == int:
        avg = (num1 + num2 + num3) / 3.0
        print "%.2f" % avg
    else:
        print "Sorry, the input(s) are invalid."

find_average (3, 4, 4)
