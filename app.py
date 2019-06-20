# print("hello world")
#
# # how code gets executed:
# print('o----')
# print(' ||||')
# # python gets executed line by line from the top
# # python interpreter: translates/inetrpret code into
# # instructions that a computer can understand
#
# print('*' * 10)
# the above is an expression- a piece of code
# that produces a value
# i need to learn django. (9-12m to become job ready)

# ~variables (temporarily store data in computer)
# price = 10
# price = 20
# print(price)
# ~booleans are like yes/no
# defining values need to be lower case
# bools = capitals

# exercise 1: we check in a patient named john
# smith- he's 20 and is a new patient
# name = 'john smith'
# age = 20
# new_patient = true

# ~input
# both input/print = in-built functions to python
# name = input('what is your name? ')
# print('hi ' + name)
# the parenthesis = calling a function/pressing a button
# on a remote control
# the above is concatenating (combining a string)
# with another string
# returns w/ what is your name? lina, "hi lina"

# exercise 2, ask two questions: a person's name
# fave color and print a message like
# "mosh likes blue"

# ~TYPE CONVERSION
# birth_year = input('Birth year: ')
# age = 2019 - int(birth_year)
# print('your age is ' + str(age))

# #~ EXERCISE 3
# Ask user for their weight, in pounds and convert it to kilograms

# weight_pounds = input('What is your weight in pounds? ')
# pounds_kg = float(weight_pounds)
# conversion_kg = (pounds_kg * 0.45)
# rounded_conversion = round(conversion_kg)
# print('you are ' + str(pounds_kg) + 'lbs which is ' + str(rounded_conversion) + 'kgs!')

# weight_pounds = input('What is your weight in pounds? ')
# # conversion_kg = float(weight_pounds) * 0.453592
# # print('you are ' + weight_pounds + 'lbs which is ' + str(int(conversion_kg)) + 'kgs!')
# #

# course = '''Python's "course" for
# beginners'''  # ''' defining strings that span multiple lines
# print(course)

# course = 'Python'
# print(course[1:-1]) # excludes the character (ie: -1) will not include n(-1)

# ~FORMATTED STRINGS (f'{}')
# first = 'John'
# last = 'Smith'
# msg = f'{first} [{last}] is a coder'
# print(msg)
# curly braces define place holders/holes for variables
# easy to visualize output

course = 'Python for Beginners'
# print(len(course)) # In this instance len is a function as it does not belong to a str/etc
# len is a function, general purpose. can be used to count numbers in a list etc
# .something is a method, when a function belongs to some kind of object/something else = method
# print(course.upper())
# the method does not alter the original but creates a new one
# print(course.find('P'))  # find method looks for the index of a str (is case sensitive)
# -1 = nothing in string

# checking the existence of a character or sequences of characters in a string
# you can use the 'in' operator
# print('Python' in course)  # this checks to see if 'python' is in the course variable.
# produces a boolean result

# print(course.upper())
# print(course.lower())
# print(course.title())  # converts each first character of a word into uppercase
# print(course.find('P'))
# print(course.replace('for', 'by'))
# help(str.title)  # to get help on methods

# ' ... ' in a string = boolean result =is a character there? yes/no

# ~Python Augmented Assignment Operator(AAO)
# eg:
# x = 10
# x = x + 3  # adds 3 to 10 = 13
# shorter version (called AAO)
# x += 3
# print(x) = 13
# can also be done with other arithmetic ie: subtract multiply etc
# x *= 3
# print(x)
# gives 30
# ~Operator precedence
# x = (10 + 3) * 2
# print(x)
# parenthesis adds priority to a calculation

# ~Math Functions
# import math
# print(math.floor(2.9))
# x = 2.9
# print(round(x))

# ABS- Absolute function isn math- returns positive representation of that value

# for complex math programs- you need to import a module.
# a module in Python is a separate file with reusable code.
# modules organize our code into different files
# eg: import math (all lower case)
# to learn more about modules eg: https://docs.python.org/3/library/math.html

# ~IF statements
#
# if it's hot(condition)
# tell user: 'drink plenty of water'
# otherwise if it's cold(condition)
# tell user: 'its a cold day, wear warm clothes'
# otherwise:(condition)'its a lovely day'
#
# price of house 1mil
# if buyer has good credit, they need to put down 10%
# otherwise
# they need to put down 20% of property
# print down the down payment for a buyer w/ good credit

#EXAMPLE~
# is_hot = False
# is_cold = False
#
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# # indented statements will be executed if the condition is true
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# # short for elseif/otherwise if
# else:
#     print("It's a lovely day")
#
# print("Enjoy your day")
#
# price = 1000000
# good_credit = False
#
# if good_credit:
#     down_payment = 0.1 * price
#     print(down_payment)
# else:
#     down_payment = 0.2 * price
#     print(f" down payment is ${down_payment}")

# ~ LOGICAL OPERATORS(for multiple conditions)
# LOGICAL/AND = operators IF/AND - combines two conditions

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible")
else:
    print("nope")

# OR - either or both conditions are true.
# AND- both conditions need to be true.