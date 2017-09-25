"""
                                                -- ASSIGNMENT 1 --
Date - 25/08/2017, 16:29 PM

The job is to create a fake passport generator. Below are the passport features :

 1. A new name
 2. A new date of birth
 3. A new ID number
 4. A print of the new information
 5. A cipher to disguise the passport

 Assumption :

 1. User may input whitespaces in the name but the system will ignore them
 2. Name cannot have numbers
 3. User input cannot be blank
 4. Age can be between 1 and 150
 5. Age cannot be text
 6. Year format is dd/mm/yyyy
 7. Entire transmission (strings) is encrypted rather than just the fields
 8. Encryption is 'n' index to the left  of the original
 9. Decryption is 'n' index to the right of the encrypted value
 10. Range of shifts in encryption is 1 to 15

 Author: Krishnendu Das
 ID: 28980980
 Email: KDAS0001@student.monash.edu

"""

# Importing the required libraries

import math
import random
import string


"""                                            Activity 1
To create a new name using two user input names, the generator will take two first names as input, and two last
names. The new name should be created by cutting each name in halves, and concatenating them together.
"""



def splitword(stringlist):

    """
    Function to split names into halves.

    It captures the length of the string and decides the position to split the name in halves. If name has odd number of
    characters, then it first decides the splitting point (split index : Ceil operation on length of the name divided
    by 2). The string is then sliced forward and backward using the split index and stored in a list. The return type
    of the function is a list.

    Input data type : String
    Output data type : List
    """

    split_list = []
    for content in stringlist:
        # calculating the split index
        split_index = int((math.ceil(len(content)) / 2))
        type(split_index)
        # slicing the name at split index
        loop_list = [content[:split_index], content[split_index:]]
        split_list = split_list + loop_list

    return split_list


def alpha_validator(text):

    """
    Function to validate if the string is empty or contains numeric values. Response code -1 indicates
    a blank or alphanumeric string where a value of 0 indicates that the string contains alphabets only

    Input data type : String
    Output data type : Number
    """

    # check if input text is blank
    if text == '':
        response_code = -1
        print("Invalid Input.")
    # check if input text contains numbers along with alphabets
    elif not text.isalpha():
        response_code = -1
        print("Name contains number. Provide correct value.")
    else:
        # if input text contains only alphabets
        response_code = 0

    return response_code


# List to store the user input - NAMES
name_list = []

# For loop to input the two first names
for i in range(1, 3):
    counter = -1
    while counter < 0:
        # whitespaces are ignored (replaced) while the user inputs the first name
        first_name = input("Enter the First Name("+str(i)+") : ").replace(" ", "")
        # Function call to validate the above input (first_name)
        counter = alpha_validator(first_name)
        if counter == 0:
            # store the correct names in a list
            name_list = name_list + [first_name]

# For loop to input two last names
for i in range(1, 3):
    counter = -1
    while counter < 0:
        # whitespaces are ignored (replaced) while the user inputs the last name
        last_name = input("Enter the Last Name("+str(i)+") : ").replace(" ", "")
        # Function call to validate the above input (first_name)
        counter = alpha_validator(last_name)
        if counter == 0:
            # store the names in a list
            name_list = name_list + [last_name]

# Split each of the four names into halves using the function splitword
mod_name_list = splitword(name_list)

""" Preparing the First Name and Last Name by manipulating the content of the list mod_name_list. Function is not used 
to generate the modified list in order to have more control over the split contents. """

new_first_name = mod_name_list[0] + mod_name_list[3]
new_last_name = mod_name_list[4] + mod_name_list[7]

# Generates the new name by concatenation
fake_name = new_first_name + ' ' + new_last_name



"""                                           Activity 2:
To create a new name using two names, the generator will take as input two first names, and two last
names. The new name should be created by cutting each name in half, and placing them together.
"""


def addmyage(age):

    """
    Function to add the digits of an age.
    The digits in the age are iterated and added consecutively into the temp_age.

    Input data type : String
    Output data type : Number
    """

    temp_age = 0
    for A in range(0, (len(age))):
        # Addition of iterated digits in temp_age
        temp_age = temp_age + int(age[A])

    return temp_age


def num_validator(text_numeral, Flag):

    """
    Function to validate if the number is empty or contains string values. Response code -1 indicates
    a blank or an alphanumeric string whereas a positive value indicates that the string contains numbers only
    Argument Flag determines if Age or Year needs to be validated. Flag = 'Age' then age is validated. Flag = 'Year'
    then year is validated.

    Input data type : String
    Output data type : Number
    """

    # Check if the text_numeral is blank
    if text_numeral == '':
        response_code = -1
        print("Empty value. Enter an age.")
    # Check if the text_numeral is numeric or not
    elif text_numeral.isnumeric() and Flag == 'Age':

            # Check the range of the text_numeral
            if int(text_numeral) in range(1, 151):
                response_code = 0
            else:
                response_code = -1
                print("Provide a correct age within range (1 - 150)")

    elif text_numeral.isnumeric() and Flag == 'Year':
        response_code = 0
    else:
        # Valid input (text_numeral)
        response_code = -1
        print("Unidentified value. Enter a correct age.")

    return response_code


# List to store the user input - AGES
age_list = []

# user input to store the two ages along with age validation. (Read assumption)
for i in range(1, 3):
    age_counter = -1
    while age_counter < 0:
        # Whitespaces are ignored (replaced) while the user inputs the age
        age = input("Enter the age(" + str(i) + ") : ").replace(" ", "")
        # Function call to validate the age inputs using function num_validator
        age_counter = num_validator(age, 'Age')
        if age_counter == 0:
            # store the ages in a list
            age_list = age_list + [age]
    # Ask the user to enter the year once both the ages are correctly entered
    if i == 2:
        year_counter = -1
        # validate the issuing year entered by the user
        while year_counter < 0:
            issuing_year = input("Enter the passport issuing year")
            # Function call to validate the above input for the year using num_validator
            year_counter = num_validator(issuing_year, 'Year')


# The new age is calculated by passing the list into the function addmyage
new_age = addmyage(age_list[0]) + addmyage(age_list[1])

# Birth year is calculated as follows : passport issuing year minus age
birth_year = int(issuing_year) - new_age

# Dictionary is defined to map the month with the number of days in it so that passport can use this
dict_month_days = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31,
                   '11': 30, '12': 31}

# A leap year  has 29 days in the month of February. Dictionary modified.
if birth_year // 4 == 0 or birth_year // 100 == 0 or birth_year // 400 == 0:
    dict_month_days['02'] = 29

# Month of birth is randomly selected from the Dictionary key in dict_month_days
birth_month = random.choice(list(dict_month_days))

# Date of birth is randomly selected from the Dictionary value for the above month key in dict_month_days
birth_date = random.randint(1, dict_month_days[birth_month])

"""The DOB is calculated concatenating the year, month and date from the above value and formatted using 02d which 
allows padding zero before single digit date."""
fake_DOB = (format(birth_date, '02d')) + '/' + format(int(birth_month), '02d') + '/' + str(birth_year)



"""                                           Activity 3:
Take the age currently on the passport and put those numbers in the ID, then add the two digits together.
The result is then modularly divided and its result is added to the ID. Repeat the process, but rather than
using the age, use the last two digits of the ID.
"""


def idsequencer(info):

    """
    Function to add the last two digits of a number

    Input data type : String
    Output data type : Number
    """

    count = 0
    added_numeral = 0

    while count < 2:
        count = count + 1
        added_numeral = added_numeral + int(info[-count])  # add the last two digits in the info
        if len(info) == 1:
            break

    return added_numeral


string_age = str(new_age)

# Generate the 10 digit sequence using the function idsequencer
while len(string_age) < 10:
    added_age = idsequencer(string_age)
    string_age = string_age + str(added_age % 10)

# Final id is stored in fake_id
fake_id = string_age



"""                                             Activity 4:
                                            Formatting the passport
The information must be presented by printing in a specific format to the console. Do this by making a string
using the following rules, then printing that string:

1) The name must appear on the First line, and the ID must be on the same line as the name, tabulated to
the right of it.
2) There must be a space between each line with text in it.
3) The second line must contain the date of birth of the individual.
4) The third line must contain the words: Authorised by followed by the name of your demonstrator for
your practical classes.
"""

# Formatting the output
output_message = "\n \nFake Passport details: \n \nName: " + fake_name + "\t \tID: " +fake_id + \
          "\n \nDate of Birth: " +fake_DOB + "\n \nAuthorised by Shirin Maghool"



"""                                           Activity 5:
Take the age currently on the passport and put those numbers in the ID, then add the two digits together.
The result is then modularly divided and its result is added to the ID. Repeat the process, but rather than
using the age, use the last two digits of the ID.
"""


def cipher(text):

    """
    Cipher the output using Caesar techniques. The output is a basic replacement of one letter for another. Each
    characters in the text are checked if they are alphabets or not. If alpha then its real position is calculated in
    the world of alphabet(lower case). This allows to calculate the index of the new alphabet by subtracting shift_key
    from the former calculated value. The case of the new alphabet is then calculated by comparing the ASCII of the
    character to convert to the ASCII of the 'Z'. If greater than the ASCII of 'Z' then its a lower case letter else an
    Upper case letter. The new letter is then produced using the ASCII of 'A' and 'a' for upper and lower case letters
    respectively.

    Input data type: String
    Output data type: String
    """

    encrypted_list = []

    for literal in text:

        # To check if the character is an alphabet or not
        if literal.isalpha():
            # Get the index of the character in the real alphabet list
            current_alpha_position = string.ascii_lowercase.index(literal.lower())
            # Get the new character shifted keyed position to the right of the alphabet list : Positive Value
            # Modulo operation facilitates the cyclic shift over 26 alphabets
            next_alpha_position = (current_alpha_position - shift_key) % alpha_range
            # Get the ASCII of the character in the text
            current_ASCII_value = ord(literal)

            # Checks if the alphabet is in lower case using ASCII value range
            if current_ASCII_value > ord('Z'):
                # Generates the ASCII of the new character (ASCII of 'a' + shifted position)
                new_ASCII_value = ord('a') + next_alpha_position
                # Generate the new character from the above ASCII value
                new_char = chr(new_ASCII_value)
            # Checks if the alphabet is in upper case using ASCII value range
            else:
                # Generates the ASCII of the new character (ASCII of 'A' + shifted position)
                new_ASCII_value = ord('A') + next_alpha_position
                # Generate the new character from the above ASCII value
                new_char = chr(new_ASCII_value)

        else:
            # Do not convert the non alpha characters
            new_char = literal
        # Form the List by converting each character from the input String
        encrypted_list = encrypted_list + [new_char]
    # Form the final message
    message_crypto = "".join(encrypted_list)

    return message_crypto


def decipher(text):

    """
    Decipher the output using Caesar techniques. The output is a basic replacement of one letter for another. Each
    characters in the text are checked if they are alphabets or not. If alpha then its real position is calculated in
    the world of alphabet(lower case). This allows to calculate the index of the new alphabet by adding shift_key
    from the former calculated value. The case of the new alphabet is then calculated by comparing the ASCII of the
    character to convert to the ASCII of the 'Z'. If greater than the ASCII of 'Z' then its a lower case letter else an
    Upper case letter. The new letter is then produced using the ASCII of 'A' and 'a' for upper and lower case letters
    respectively.

    Input data type: String
    Output data type: String

    """

    encrypted_list = []

    for literal in text:

        # To check if the character is an alphabet or not
        if literal.isalpha():
            # Get the index of the character in the real alphabet list
            current_alpha_position = string.ascii_lowercase.index(literal.lower())
            # Get the new character shifted keyed position to the left of the alphabet list : Negative value
            # Modulo operation facilitates the cyclic shift over 26 alphabets
            next_alpha_position = ((current_alpha_position + shift_key) % alpha_range)
            # Get the ASCII of the character in the text
            current_ASCII_value = ord(literal)

            # Checks if the alphabet is in lower case using ASCII value range
            if current_ASCII_value > ord('Z'):
                # Generates the ASCII of the new character (ASCII of 'a' + shifted position)
                new_ASCII_value = ord('a') + next_alpha_position
                # Generate the new character from the above ASCII value
                new_char = chr(new_ASCII_value)
            else:
                # Generates the ASCII of the new character (ASCII of 'A' + shifted position)
                new_ASCII_value = ord('A') + next_alpha_position
                # Generate the new character from the above ASCII value
                new_char = chr(new_ASCII_value)
        else:
            # Do not convert the non alpha characters
            new_char = literal
        # Form the List by converting each character from the input String
        encrypted_list = encrypted_list + [new_char]
    # Form the final message
    message_crypto = "".join(encrypted_list)

    return message_crypto



alpha_range = 26
shift_key = random.randint(1, 15)
message_ciphered = cipher(output_message)
print(message_ciphered)

# User input to Decipher the encrypted message
user_choice = input('\n' + 'Type Q to Quit or D to Decipher the above message').upper()
# Define the valid inputs
user_options = ['Q', 'D']

# user selects an invalid input
if user_choice not in user_options:
    print('\n' + "Invalid selection, please retry using valid options")
    # user decides to quit
elif user_choice == 'Q':
    print('\n' + "Thanks for faking it !! ")
else:
    # user decides to decipher the message
    message_deciphered = decipher(message_ciphered)
    print('\n' + 'The original message was encrypted by {0} shifts to the left.'.format(shift_key))
    print(message_deciphered)

# end