#Source : https://agilekatas.co.uk/katas/FizzBuzz-Kata

#Feature 1 : Basic Fizz Buzz Scoring
#------------------------------------

#Normal Numbers Return Same Number
def enter_number(input):
	return input

#Multiples of Three Return Fizz
def fizz(input):
	if enter_number(input) % 3 == 0: return True

#Multiples of Five Return Buzz
def buzz(input):
	if enter_number(input) % 5 == 0: return True

#Multiples of Three and Five Return Fizz Buzz
def fizz_buzz(input):
	if fizz(input) and buzz(input): return "fizz buzz"
	elif fizz(input): return "fizz"
	elif buzz(input): return "buzz"
	else: return enter_number(input)
	
if __name__ == '__main__':
	input = int(input("Please enter a number : "))	
	print(fizz_buzz(input))
