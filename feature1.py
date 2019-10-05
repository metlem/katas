#Source : https://agilekatas.co.uk/katas/FizzBuzz-Kata

#Feature 1 : Basic Fizz Buzz Scoring

input = int(input("Please enter a number : "))

#----------------------------------------------------------------------
#Normal Numbers Return Same Number
"""	As a games designer 
	I want a normal number to return that number
	So that the game can be scored according to the rules.

		Given I have started the game.
		When I enter $number
		Then $result is returned
"""

def enter_number(input):
	return input


print("You entered the number : {} ".format(enter_number(input)))

#------------------------------------------------------------------------
#Multiples of Three Return Fizz
"""	As a games designer
	I want a multiple of three to return 'fizz'
	So that the game can be scored according to the rules
"""

def fizz(input):
	if input % 3 == 0:
		return "fizz"

print("{} → {}".format(input, fizz(input)))

#------------------------------------------------------------------------
#Multiples of Five Return Buzz
"""	As a games designer
	I want a multiple of five to return 'buzz'
	So that the game can be scored according to the rules
"""

def buzz(input):
	if input % 5 == 0:
		return "buzz"

print("{} → {}".format(input, buzz(input)))

#------------------------------------------------------------------------
#Multiples of Three and Five Return Fizz Buzz
"""	As a games designer
	I want a multiple of three and five to return 'fizz buzz'
	So that the game can be scored according to the rules
"""

def fizz_buzz(input):
	if input % 3 == 0 and input % 5 == 0:
		return "fizz buzz"

print("{} → {}".format(input, fizz_buzz(input)))