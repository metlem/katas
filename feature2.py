#Source : https://agilekatas.co.uk/katas/FizzBuzz-Kata


#Feature 2 : Playing FizzBuzz Variations
#----------------------------------------

#Normal Numbers Return Same Number
def enter_number(input):
	return input

#Multiples of Three Return Fizz
def fizz(input):
	if enter_number(input) % 3 == 0: return True

#Multiples of Five Return Buzz
def buzz(input):
	if enter_number(input) % 5 == 0: return True

#Multiples of Seven Return Pop
def pop(input):
	if enter_number(input) % 7 == 0: return True

#Multiples of Three and Five Return Fizz Buzz
def fizz_buzz_pop(input):
	if fizz(input) and buzz(input) and pop(input): return "fizz buzz pop"
	elif fizz(input) and buzz(input): return "fizz buzz"
	elif fizz(input) and pop(input) : return "fizz pop"
	elif buzz(input) and pop(input) : return "buzz pop"	
	elif fizz(input): return "fizz"
	elif buzz(input): return "buzz"
	elif pop(input) : return "pop"
	else: return enter_number(input)
	
if __name__ == '__main__':
	input = int(input("Please enter a number : "))	
	print(fizz_buzz_pop(input))










