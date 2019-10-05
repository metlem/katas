#Source : https://agilekatas.co.uk/katas/FizzBuzz-Kata

#Feature 3 : Creating Fizz Buzz Variations

input = int(input("Please enter a number : "))

#----------------------------------------------------------------------
#Using a Custom Substitution
"""As a player
	I want to be able to choose my own substitutions
	So that I can tailor the game to my preferences

		Given I have substituted multiples of two for 'fuzz'
		When I enter $number
		Then $result is returned
"""
def hav_hav(input):
	if input % 2 == 0:
		return "hav hav"
	else:
		return input

#print("{} → {}".format(input, hav_hav(input)))

#----------------------------------------------------------------------
#Linking Custom Substitutions Together
"""As a player
	I want my substitutions to work the same way as Fizz Buzz
	So that the essence of the game remains the same

		Given I have substituted multiples of two for 'fuzz'
		And I have substituted multiples of three for 'bizz'
		When I enter $number
		Then $result is returned
"""
def hav_vız(input):
	if input % 2 == 0 and input % 3 == 0:
		return "hav hav vız vız"
	elif input % 2 == 0:
		return "hav hav"
	elif input % 3 == 0:
		return "vız vız"
	
	else:
		return input

print("{} → {}".format(input, hav_vız(input)))
