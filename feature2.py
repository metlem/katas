#Source : https://agilekatas.co.uk/katas/FizzBuzz-Kata

#Feature 2 : Playing FizzBuzz Variations

input = int(input("Please enter a number : "))

#----------------------------------------------------------------------
#Multiples of Seven Return Pop
"""As a games designer
	I want a multiple of seven to return 'pop'
	So that the game can be scored according to the rules
		
		Given I have started the game
		When I enter $number
		Then $result is returned
"""
def pop(input):
	if input % 7 == 0:
		return "pop"

print("{} → {}".format(input, pop(input)))

#----------------------------------------------------------------------
#Multiples of Three and Seven Return Fizz Pop
"""As a games designer
	I want a multiple of three and seven to return 'fizz pop'
	So that the game can be scored according to the rules
"""

def fizz_pop(input):
	if input % 3 == 0 and input % 7 == 0 :
		return "fizz pop"

print("{} → {}".format(input, fizz_pop(input)))

#----------------------------------------------------------------------
#Multiples of Five and Seven Return Buzz Pop
"""As a games designer
	I want a multiple of five and seven to return 'buzz pop'
	So that the game can be scored according to the rules
"""
def buzz_pop(input):
	if input % 5 == 0 and input % 7 == 0 :
		return "buzz pop"

print("{} → {}".format(input, buzz_pop(input)))


#----------------------------------------------------------------------
#Multiples of Three, Five and Seven Return Fizz Buzz Pop
"""As a games designer
	I want a multiple of three, five and seven to return 'fizz buzz pop'
	So that the game can be scored according to the rules
"""
def fizz_buzz_pop(input):
	if input % 3 == 0 and input % 5 == 0 and input % 7 == 0 :
		return "fizz buzz pop"

print("{} → {}".format(input, fizz_buzz_pop(input)))
