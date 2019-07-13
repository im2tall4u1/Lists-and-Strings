"""
Author:	Eric Zair
File:	list_reversal.py
Description:	This program allows the user to enter a list of their
				chosing and reverse it.
				Example:	If the user enters: [10, 20, 30],
							Then the program will output: [30, 20, 10]
"""


def get_reversed_list(list_given_by_user):
	"""
	Desc: This function takes a list object reverses it.
	:param list_given_by_user: List given by the user that will be reversed.
	:type list_given_by_user: list
	:return list: this is the list given by the user, but in revered order.
	"""
	return list_given_by_user[::-1]


def worse_way_to_reverse_list(list_given_by_user):
	"""
	Desc: This function takes a list object reverses it.
	:param list_given_by_user: List given by the user that will be reversed.
	:type list_given_by_user: list
	:return list: this is the list given by the user, but in revered order.
	"""
	return [list_element for list_element in list_given_by_user]


def even_worse_way_to_reverse_list(list_given_by_user):
	"""
	Desc: This function takes a list object reverses it.
	:param list_given_by_user: List given by the user that will be reversed.
	:type list_given_by_user: list
	:return list: this is the list given by the user, but in revered order.
	"""
	revered_user_list = []
	for list_element in list_given_by_user:
		revered_user_list.append(list_element)
	return revered_user_list


def main():
	"""
	NOTES FOR @Trent:	Make sure to keep your program organized. Use functions, break
						functionality up, so that things are easier to deal with.
						Comment your methods. Don't just write code only in the main.
						USE GOOD VARIABLE NAMES! x is not a good variable name, as it does
						not tell me anything about what x really is, or what it represents.
						Long variables names are not a bad thing. Same thing with function
						names. Finally, Always give your methods a header, it tells the user
						the type of each thing, what the params are, and what the expected 
						return type and what that return type should be associated with :)
	"""
	print("Exit the program by typing \"quit\" (without quotes).\n"
		  "Enter \"reverse\" (without quotes) in order to display the reversed the list")
	user_list = []
	
	# Allow the user to keep entering string values into a list.
	# The can then display the list in reverse, or exit the program.
	while True:
		user_input_string = input("Enter a value to append to the list: ")
		if user_input_string.strip() == 'quit':
			print("Have a good day.")
			exit(0)
		elif user_input_string.strip() == 'reverse':
			print("Reversed list:", get_reversed_list(user_input_string))
		else:
			user_input_string.append(user_input_string)


if __name__ == '__main__':
	main()