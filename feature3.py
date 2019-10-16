#Source : https://agilekatas.co.uk/katas/FizzBuzz-Kata

#Feature 3 : Creating Fizz Buzz Variations
#------------------------------------------

#Using a Custom Substitution
def enter_number(input):
	return input

def hello(input):
	if enter_number(input) % 2 == 0: return True

def hi(input):
	if enter_number(input) % 3 == 0: return True 

#Linking Custom Substitutions Together
def hello_hi(input):
	if hello(input) and hi(input):	return "merhabalar selamlar"
	elif hello(input):	return "merhabalar"
	elif hi(input):	return "selamlar"
	else: return enter_number(input)


if __name__ == '__main__':
	input = int(input("Please enter a number : "))	
	print(hello_hi(input))

