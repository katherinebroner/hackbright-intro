print "Welcome to the survey!"
name = raw_input("What is your name? ")
color = raw_input("What is your favorite color? ")
hobby = raw_input("What is your favorite hobby? ")
movie = raw_input("What is your favorite movie? ")
book = raw_input("What is your favorite book? ")
animal = raw_input("What is your favorite animal? ")
#print "%s's favorite color is %s." % (name, color)
#print "%s's favorite hobby is %s." % (name, hobby)
#print "%s's favorite movie is %s." % (name, movie)
#print "%s's favorite book is %s." % (name, book)
#print "%s's favorite animal is %s." % (name, animal)                                             

def print_survey_results(name,color,hobby,movie,book,animal):
	print "%s's favorite color is %s." % (name, color)
	print "%s's favorite hobby is %s." % (name, hobby)
	print "%s's favorite movie is %s." % (name, movie)
	print "%s's favorite book is %s." % (name, book)
	print "%s's favorite animal is %s." % (name, animal) 

print_survey_results (name, color, hobby, movie, book, animal)
